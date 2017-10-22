import random
import datetime
import bisect

from .models import UserInfo


from django.core.files import File

from django.contrib.auth.models import User
from django.test import TestCase
# Create your tests here.


def populate():

    signs = [(1,20,"capricorn"), (2,18,"aquarius"), (3,20,"pisces"), (4,20,"aries"),
             (5,21,"taurus"), (6,21,"gemini"), (7,22,"cancer"), (8,23,"leo"),
             (9,23,"virgo"), (10,23,"libra"), (11,22,"scorpio"), (12,22,"sagittarius"),
             (12,31,"capricorn")]

    def zodiac_image(date):
        zodiac = signs[bisect.bisect(signs,(date.month, date.day))][2]
        return f'media/default/{zodiac}.png'

    names = [
        ('female', 'Lucie',     'Manette'),
        (  'male', 'James',     'Striker'),
        ('female', 'Elizabeth', 'Ocelot'),
        ('female', 'Charlotte', 'Bartholomew'),
        ('female', 'Rossie',    'Maudner'),
        ('female', 'Agatha',    'Christie'),
        ('female', 'Maya',      'Angelou'),
        (  'male', 'Charles',   'Blue'),
        (  'male', 'Richard',   'Flyndermann')
    ]
    for gender, first, last in names:
        user = User.objects.create_user(
            username  = last.lower(),
            password  = 'animagus',
            email     = 'aliasmanette@gmail.com',
            first_name= first,
            last_name = last)

        year = random.randrange(1980, 2000)
        date = random.randrange(356)        
        date = datetime.date(year, 1, 1) + datetime.timedelta(date)
        path = zodiac_image(date)

        info = UserInfo.objects.create(
                picture   = File(open(path, 'rb')),
                user      = user,
                gender    = gender,
                interest  = 'books',
                birthdate = date)
        user.save()
        info.save()
        