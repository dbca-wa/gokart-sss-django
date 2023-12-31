# Generated by Django 4.2.3 on 2023-11-20 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0006_alter_proxycache_created_alter_userprofile_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='BomSyncList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
