# Generated by Django 4.2.7 on 2023-12-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0010_alter_catalogue_keywords_alter_catalogue_legend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
