from django.contrib import admin
from django.urls import path
from Article import views


urlpatterns = [
    path('',views.index,name='index')
]
