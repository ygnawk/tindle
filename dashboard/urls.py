


from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = "dashboard"
urlpatterns = [
    url(r'^$', views.index, name="index"),
]
