# Generated by Django 5.0.1 on 2024-01-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawPatrol', '0014_favorito'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorito',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='Herores'),
        ),
    ]