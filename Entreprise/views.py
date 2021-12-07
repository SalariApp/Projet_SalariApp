from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Info_Entreprise(request):
    return HttpResponse('Bienvenue dans la Liste des Entreprises')