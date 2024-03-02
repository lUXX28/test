from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("This is the index page")

def dash(request):
    return render(request, 'dashboard.html')

def login(request):
    users = {
        'admin':'admin'
    }
    inputUsername = request.POST.get('username')
    inputPassword = request.POST.get('password')
    if inputPassword == users[inputUsername]:
        return HttpResponse("Login success")
    else:
        return HttpResponse("Login error")
def profile(request):
    return HttpResponse("this is profile page")
