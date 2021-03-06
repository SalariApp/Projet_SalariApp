# Generated by Django 4.0 on 2022-01-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEntreprise', models.CharField(max_length=50, null=True)),
                ('anneeCreation', models.IntegerField(max_length=4)),
                ('activite', models.CharField(max_length=100, null=True)),
                ('effectif', models.IntegerField(null=True)),
                ('capital', models.IntegerField(null=True)),
                ('nomDirecteur', models.CharField(max_length=50, null=True)),
                ('numeroContribuable', models.IntegerField(null=True)),
                ('formeJuridique', models.CharField(choices=[('SA', 'SA'), ('SARL', 'SARL'), ('SP', 'SP')], max_length=50, null=True)),
                ('chiffreAffaire', models.IntegerField(null=True)),
            ],
        ),
    ]
