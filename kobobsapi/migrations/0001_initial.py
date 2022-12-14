# Generated by Django 4.1 on 2022-08-07 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Envoies_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_expediteur', models.CharField(default='', max_length=100)),
                ('postnom_expediteur', models.CharField(default='', max_length=100)),
                ('prenom_expediteur', models.CharField(default='', max_length=100)),
                ('email_expediteur', models.CharField(default='', max_length=100)),
                ('numero_expediteur', models.CharField(default='', max_length=100)),
                ('pays_expediteur', models.CharField(default='', max_length=100)),
                ('nom_beneficiaire', models.CharField(default='', max_length=100)),
                ('postnom_beneficiaire', models.CharField(default='', max_length=100)),
                ('prenom_beneficiaire', models.CharField(default='', max_length=100)),
                ('adresse_beneficiare', models.CharField(default='', max_length=100)),
                ('numero_beneficiaire', models.CharField(default='', max_length=100)),
                ('pays_beneficiaire', models.CharField(default='', max_length=100)),
                ('montant_envoie', models.DecimalField(decimal_places=2, max_digits=15)),
                ('frais_envoie', models.DecimalField(decimal_places=2, max_digits=15)),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('code_retrait', models.CharField(max_length=8, null=True, unique=True)),
                ('data_operation', models.DateField(auto_now_add=True)),
                ('date_heure_operation', models.DateTimeField(auto_now_add=True)),
                ('code_abonne', models.CharField(max_length=5, null=True, unique=True)),
                ('status_retrait', models.CharField(default='retrait en attente', max_length=30)),
                ('agent_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
