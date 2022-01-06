from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Login (request):
    return render(request, 'Compte/Login.html')

def Inscription (request):
    return render(request, 'Compte/Inscription.html')