# Generated by Django 5.0.8 on 2024-11-12 07:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0023_alter_proxy_password_alter_proxy_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpatialDataCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bfrs', models.CharField(max_length=500)),
                ('calculation_status', models.CharField(choices=[('Imported', 'Imported'), ('Processing Finalised', 'Processing Finalised'), ('Failed', 'Failed'), ('Completed', 'Completed')], default='Imported', max_length=40, verbose_name='Calculation Status')),
                ('features', models.TextField(blank=True, null=True)),
                ('options', models.TextField(blank=True, null=True)),
                ('output', models.TextField(blank=True, null=True)),
                ('user', models.CharField(max_length=500, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
