# Generated by Django 2.2.17 on 2021-03-23 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20210323_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='time_limit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='total_mark',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('time_started', models.DateTimeField(auto_now_add=True)),
                ('time_finished', models.DateTimeField(auto_now=True)),
                ('time_elapsed', models.DateTimeField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='core.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
