import datetime
from bisect import bisect

from .models import UserInfo, Book, Preference

import django.contrib as contrib
from django.core.files import File
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.images import ImageFile


from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

def index(request):
    return HttpResponseRedirect('/user/profile')

@login_required
def profile(request):
    return render(request, 'user/profile.html', {
        'user': request.user,
        'rated' : request.user.preference_set.all()
    })



def auth(request):

    post = request.POST
    user = authenticate(request, username=post['username'], password=post['password'])
    referer = request.META.get('HTTP_REFERER')
    if user is None:
        return HttpResponseRedirect(referer)
    contrib.auth.login(request, user)

    link = request.POST.get('next', '/user/profile')
    return HttpResponseRedirect(link)



def login_page(request):
    user = request.user
    if user.is_authenticated():
        return HttpResponseRedirect('/user/profile')
    else:
        return render(request, 'user/login.html', {'next' : request.GET.get('next', '')})

def register(request):
    user = request.user
    if user.is_authenticated():
        return HttpResponseRedirect('/user/profile')
    return render(request, 'user/register.html')



def _create(info_dict): 

    signs = [(1,20,"capricorn"), (2,18,"aquarius"), (3,20,"pisces"), (4,20,"aries"),
             (5,21,"taurus"), (6,21,"gemini"), (7,22,"cancer"), (8,23,"leo"),
             (9,23,"virgo"), (10,23,"libra"), (11,22,"scorpio"), (12,22,"sagittarius"),
             (12,31,"capricorn")]

    def zodiac_image(birthdate):
        date = datetime.datetime.strptime(birthdate, r'%Y-%m-%d')
        zodiac = signs[bisect(signs,(date.month, date.day))][2]
        return f'media/default/{zodiac}.png'


    user = User.objects.create_user(
            username   = info_dict['username'].lower(),
            password   = info_dict['password'],
            email      = info_dict['email'],
            first_name = info_dict['name_first'],
            last_name  = info_dict['name_last'])

    path = zodiac_image(info_dict['birthdate'])
    info = UserInfo.objects.create(
            user      = user,
            picture   = File(open(path, 'rb')),
            gender    = info_dict['gender'],
            interest  = info_dict['interest'],
            birthdate = info_dict['birthdate'])

    user.save()
    info.save()


def create(request):
    post = request.POST
    assert(post['password'] == post['confirm'])

    _create(post)

    return HttpResponseRedirect('/user/login')


def logout(request):
    contrib.auth.logout(request)
    return HttpResponseRedirect('/user/login')


def get_queue(user):
    pass

@login_required
def search(request):

    def annotate(user, queryset):
        rates = {preference.book: preference.rating 
                for preference in user.preference_set.all()}
        books = [book for book in queryset]
        for book in books:
            if book in rates:
                book.rating = int(rates[book])
            else:
                book.rating = 0
        return books



    text = request.GET['query']
    user = request.user
    return render(request, 'user/search.html', {
        'user'   : request.user,
        'isbn'   : annotate(user, Book.objects.filter(isbn__search   = text)),
        'author' : annotate(user, Book.objects.filter(author__search = text)),
        'title'  : annotate(user, Book.objects.filter(title__search  = text))
    })



def rate(request):
    book = Book.objects.get(id = request.POST['bookid'])
    preference = request.user.preference_set.filter(book = book)
    if len(preference):
        if preference[0].rating == 1 + int(request.POST['rating']):
            preference.delete()
        else:
            preference[0].rating = 1 + int(request.POST['rating'])
            preference[0].save()
    else:
        Preference.objects.create(
            user = request.user,
            rating = 1 + int(request.POST['rating']),
            book   = book)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])