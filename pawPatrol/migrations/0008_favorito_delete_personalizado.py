# Generated by Django 5.0.1 on 2024-01-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawPatrol', '0007_personalizado'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('habilidad', models.CharField(max_length=70)),
                ('raza', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=300)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='heroes')),
            ],
        ),
        migrations.DeleteModel(
            name='personalizado',
        ),
    ]
