from django.db import models

# Create your models here.

class Compte(models.Model):
    nomEntre = models.CharField(max_length=20, null=True)
    passwd = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.nomEntre