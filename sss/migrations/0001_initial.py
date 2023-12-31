# Generated by Django 4.2.3 on 2023-08-10 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('PHS', 'Perth Hills'), ('SWC', 'Swan Coastal'), ('BWD', 'Blackwood'), ('WTN', 'Wellington'), ('DON', 'Donnelly'), ('FRK', 'Frankland'), ('ALB', 'Albany'), ('ESP', 'Esperance'), ('EKM', 'East Kimberley'), ('WKM', 'West Kimberley'), ('EXM', 'Exmouth'), ('PIL', 'Pilbara'), ('KAL', 'Kalgoorlie'), ('GER', 'Geraldton'), ('MOR', 'Moora'), ('SHB', 'Shark Bay'), ('GSN', 'Great Southern'), ('CWB', 'Central Wheatbelt'), ('SWB', 'Southern Wheatbelt')], max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('kimberley', 'Kimberley'), ('pilbara', 'Pilbara'), ('midwest', 'Midwest'), ('goldfields', 'Goldfields'), ('swan', 'Swan'), ('wheatbelt', 'Wheatbelt'), ('south west', 'South West'), ('warren', 'Warren'), ('south coast', 'South Coast')], default=None, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sss.district')),
                ('region_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sss.region')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sss.region'),
        ),
    ]
