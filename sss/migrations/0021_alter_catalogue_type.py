# Generated by Django 4.2.8 on 2023-12-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0020_catalogue_workspace_alter_catalogue_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='type',
            field=models.CharField(blank=True, choices=[('', 'None'), ('TileLayer', 'TileLayer'), ('TileLayer2', 'TileLayer2'), ('TileWMSLayer', 'TileWMSLayer'), ('WMSLayer', 'WMSLayer'), ('ImageLayer', 'ImageLayer')], default='', help_text='Map Server Type TileLayer, ImageLayer, WMSLayer etc', max_length=128, null=True),
        ),
    ]
