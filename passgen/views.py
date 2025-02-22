from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return HttpResponse("<h2>Hello World</h2> <br> <h4> I am Martin Githae, Python Engineer, AI and Machine Learning Expert</h4>") 

def passgen(request):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ""
    for x in range(15):
        password += random.choice(char)

    pass_dict = {'password': password}
    return JsonResponse(pass_dict)