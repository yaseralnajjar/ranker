# Generated by Django 2.2.17 on 2021-03-23 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_test_time_limit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='time_limit',
            new_name='time_limit_mins',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='time_limit',
            new_name='time_limit_mins',
        ),
    ]