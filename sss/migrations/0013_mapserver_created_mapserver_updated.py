# Generated by Django 4.2.7 on 2023-12-11 09:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0012_mapserver_catalogue_map_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapserver',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='mapserver',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]