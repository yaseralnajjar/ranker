# Generated by Django 3.2.10 on 2021-12-10 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='time_limit_mins',
        ),
    ]