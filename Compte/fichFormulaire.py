from django.forms import ModelForm

from Compte.models import Compte


class Comptef(ModelForm):
    class Meta:
        model= Compte
        fields="__all__"