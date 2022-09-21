# Generated by Django 4.1 on 2022-09-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobobsapi', '0013_remove_envoies_data_adresse_beneficiaire_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envoies_data',
            name='email_expediteur',
        ),
        migrations.RemoveField(
            model_name='envoies_data',
            name='postnom_beneficiaire',
        ),
        migrations.RemoveField(
            model_name='envoies_data',
            name='postnom_expediteur',
        ),
        migrations.AlterField(
            model_name='envoies_data',
            name='code_retrait',
            field=models.CharField(max_length=9, null=True, unique=True),
        ),
    ]