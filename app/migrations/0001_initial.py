# Generated by Django 4.2.6 on 2023-11-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trial_input_1', models.CharField(default=None, max_length=255, null=True)),
                ('trial_input_2', models.IntegerField(default=None, null=True)),
                ('trial_input_3', models.TimeField(default=None, null=True)),
            ],
        ),
    ]