# Generated by Django 5.0.1 on 2024-01-27 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pawPatrol', '0015_favorito_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorito',
            name='foto',
        ),
    ]
