# Generated by Django 5.0.1 on 2024-01-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawPatrol', '0011_favorito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorito',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]