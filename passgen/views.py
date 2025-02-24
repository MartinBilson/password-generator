from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def passgen(request):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ""
    for x in range(15):
        password += random.choice(char)

    pass_dict = {'password': password}
    return JsonResponse(pass_dict)