
from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = "user"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^login/$', views.login_page, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^create/$', views.create, name="create"),
    url(r'^auth/$', views.auth, name="auth"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^search/$', views.search, name="search"),
    url(r'^rate/$', views.rate, name="rate"),
]
