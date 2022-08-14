# Generated by Django 4.1 on 2022-08-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobobsapi', '0003_rename_adresse_beneficiare_envoies_data_adresse_beneficiaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envoies_data',
            name='montant_device',
        ),
        migrations.RemoveField(
            model_name='envoies_data',
            name='montant_envoie',
        ),
        migrations.AddField(
            model_name='envoies_data',
            name='adresse_expediteur',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='envoies_data',
            name='frais_tva',
            field=models.DecimalField(decimal_places=2, default='', max_digits=15),
        ),
        migrations.AddField(
            model_name='envoies_data',
            name='montant_beneficiaire',
            field=models.DecimalField(decimal_places=2, default='', max_digits=15),
        ),
        migrations.AddField(
            model_name='envoies_data',
            name='montant_envoie_sans_frais',
            field=models.DecimalField(decimal_places=2, default='', max_digits=15),
        ),
        migrations.AlterField(
            model_name='envoies_data',
            name='status_retrait',
            field=models.CharField(default='code retrait en attente de validation', max_length=50),
        ),
    ]