# Generated by Django 4.1 on 2022-09-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobobsapi', '0017_alter_envoies_data_data_operation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envoies_data',
            name='data_operation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='envoies_data',
            name='date_heure_operation',
            field=models.CharField(default='', max_length=50),
        ),
    ]
