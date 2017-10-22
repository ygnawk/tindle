

from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models




class UserInfo(models.Model):
    picture     = models.ImageField()
    user        = models.OneToOneField(User)
    description = models.TextField(default="")
    birthdate   = models.DateField()
    interest    = models.CharField(max_length=6)
    gender      = models.CharField(max_length=6)


    def __str__(self):
        return str(f"{self.user}")


class Book(models.Model):

    published = models.CharField(max_length=10)
    author    = models.CharField(max_length=1000)
    title     = models.CharField(max_length=1000)
    isbn      = models.CharField(max_length=1000)
    imageurl  = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"


class Preference(models.Model):
    modified = models.DateTimeField(auto_now=True)
    created  = models.DateTimeField(auto_now_add=True)
    book     = models.OneToOneField(Book, on_delete=models.PROTECT)
    user     = models.ForeignKey(User, on_delete=models.PROTECT)
    rating   = models.PositiveIntegerField(validators=[
        MinValueValidator(1), 
        MaxValueValidator(10)
    ])

    def __str__(self):
        return f"({self.user.username}, {self.book}, {self.rating})"




