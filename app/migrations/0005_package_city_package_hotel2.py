# Generated by Django 4.2.6 on 2023-11-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_festival_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='package',
            name='hotel2',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]
