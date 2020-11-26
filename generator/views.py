from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def eggs(request):
    return HttpResponse("Eggs are so tasty, is'nt it")

def about_page(request):
    return render(request, 'generator/about.html')

def password(request):
    length=int(request.GET.get('length'))
    needUpper=request.GET.get('upperCase')
    needNumber = request.GET.get('numbers')
    needSpecialChar=request.GET.get('specialChar')

    thegeneratedPassword=''

    charactersList=list('qwertyuiopasdfghjklzxcvbnm')
    if(needUpper):
        charactersList.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if(needNumber):
        charactersList.extend(list('01234567890'))

    if(needSpecialChar):
        charactersList.extend('~!@#$%^&*()')

    if (length != 0):
        if(length <= 15):
            for x in range(length):
                thegeneratedPassword += random.choice(charactersList)
        else:
            thegeneratedPassword = 'Length Selected is greater than 15 Error'
    else:
        thegeneratedPassword = 'Length Selected is 0 Error'

    return render(request, "generator/password.html", {'password':thegeneratedPassword})