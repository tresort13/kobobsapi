# Generated by Django 4.1 on 2022-08-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobobsapi', '0005_alter_envoies_data_frais_tva_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='envoies_data',
            old_name='montant_device',
            new_name='adresse_expediteur',
        ),
        migrations.RemoveField(
            model_name='envoies_data',
            name='montant_envoie',
        ),
        migrations.AlterField(
            model_name='envoies_data',
            name='status_retrait',
            field=models.CharField(default='code retrait en attente de validation', max_length=50),
        ),
    ]
