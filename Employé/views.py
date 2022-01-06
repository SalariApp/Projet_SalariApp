from django.shortcuts import render
from django.http import HttpResponse
from Employé.models import Employé
from Entreprise.models import Entreprise
# Create your views here.

def Liste_Employé (request):
    Employés=Employé.objects.all()
    Entreprises=Entreprise.objects.all()
    context={'Entreprises':Entreprises}
    return render(request,'Entreprise/entreprise.html',context)