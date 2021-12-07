from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Liste_Employé (request):
    return HttpResponse('Bienvenue dans la liste de employés')