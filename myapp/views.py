from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,"home.html",{})

def about(request):
    User={
        'Name':"Tahesin Yusuf Khatik",
        'Email':"tahasinkhatik02@gmail.com",
        'Username':"Tahas1994",
        'About':"Hello I am Tahesin Khatik from Shirpur",
        'isActive':True,
        'Phone':"8668819041"
    }
    data={
        'User':User
    }
    return render(request, "about.html", data)