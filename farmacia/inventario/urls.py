#from django.conf.urls import url
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),

]
