# Generated by Django 4.1 on 2022-09-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobobsapi', '0014_remove_envoies_data_email_expediteur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='envoies_data',
            name='email_expediteur',
            field=models.CharField(default='', max_length=100),
        ),
    ]
