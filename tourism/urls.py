from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls import include,url

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^hillStations/',views.hillStations,name="hillStations"),
    url(r'^hillStations/details/',views.details,name="details"),
]
