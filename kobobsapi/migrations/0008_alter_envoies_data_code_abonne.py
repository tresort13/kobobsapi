# Generated by Django 4.1 on 2022-08-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobobsapi', '0007_envoies_data_frais_tva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envoies_data',
            name='code_abonne',
            field=models.CharField(max_length=5, null=True),
        ),
    ]