from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request,"generator/home.html")

def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    password = ""
    length = int(request.GET.get("length"))
    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLNMNOPQRSTUVWXYZ")
    if request.GET.get('numbers'):
        characters.extend("0123456789")
    if request.GET.get('special'):
        characters.extend("!@#$%^&*()")

    for x in range(length):
        password +=random.choice(characters)
    return render(request,"generator/password.html",{
        "password":password
        })


def about(request):
    return render(request, "generator/about.html")