# Generated by Django 2.2.17 on 2021-03-23 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210323_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='users_chosen',
            field=models.ManyToManyField(blank=True, related_name='chosen_answers', to=settings.AUTH_USER_MODEL),
        ),
    ]