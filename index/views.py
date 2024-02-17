from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(requests):
    return HttpResponse("<a /href=\"/login\">login</a>")

def hallo(requests):
    return HttpResponse("123")

def user(requests):
    return HttpResponse("This is user page")