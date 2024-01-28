# Generated by Django 5.0.1 on 2024-01-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='heroe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('habilidad', models.CharField(max_length=70)),
                ('raza', models.CharField(max_length=40)),
                ('vehiculo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('propietario', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='villano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('raza', models.CharField(max_length=40)),
                ('vehiculo', models.CharField(max_length=40)),
            ],
        ),
    ]
