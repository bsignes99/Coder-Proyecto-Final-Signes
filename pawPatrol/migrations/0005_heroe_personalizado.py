# Generated by Django 5.0.1 on 2024-01-26 00:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawPatrol', '0004_delete_heroe_personalizado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='heroe_personalizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('habilidad', models.CharField(max_length=70)),
                ('raza', models.CharField(max_length=40)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='heroes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
