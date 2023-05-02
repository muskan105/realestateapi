# Generated by Django 3.2.18 on 2023-03-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghar',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='ghar',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
