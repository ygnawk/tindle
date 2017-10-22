from django.contrib import admin

# Register your models here.

from .models import Preference, Book, UserInfo

admin.site.register(Book)
admin.site.register(UserInfo)
admin.site.register(Preference)


