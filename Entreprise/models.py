from django.db import models

# Create your models here.

class Entreprise(models.Model):
    FORMEJURIDIQUE = (('SCS','SCS'),
                      ('SNC','SNC'),
                      ('SARL', 'SARL'),
                      ('SA','SA'),
                      ('SAS', 'SAS'),
                      ('GIE', 'GIE'),
                      ('SEP', 'SEP'),
                      ('SCP', 'SCP'),
                      ('SCI', 'SCI'),
                      ('SP','SP'))
    nomEntreprise = models.CharField(max_length=50, null=True)
    anneeCreation = models.IntegerField(null=True)
    activite = models.CharField(max_length=100, null=True)
    effectif = models.IntegerField(null=True)
    capital = models.IntegerField(null=True)
    nomDirecteur = models.CharField(max_length=50, null=True)
    numeroContribuable = models.IntegerField(null=True)
    formeJuridique = models.CharField(max_length=50, null=True, choices=FORMEJURIDIQUE)
    chiffreAffaire =models.IntegerField(null=True)

    def __str__(self):
        return self.nomEntreprise