from django.shortcuts import render
from django.http import HttpResponse
from Entreprise.models import Entreprise
# Create your views here.

def Info_Entreprise (request):
    Entreprises=Entreprise.objects.all()
    context={'Entreprises':Entreprises}
    return render(request,'Entreprise/entreprise.html',context)
