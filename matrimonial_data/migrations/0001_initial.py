# Generated by Django 3.2.18 on 2023-03-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ghar',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('image', models.URLField(null=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('name', models.TextField(default='')),
            ],
        ),
    ]
