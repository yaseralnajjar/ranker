# Generated by Django 3.2.10 on 2021-12-09 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questionchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='core.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='core.tag'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='core.test'),
        ),
        migrations.AddField(
            model_name='answerchoice',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answerchoice',
            name='chosen_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questionchoice'),
        ),
        migrations.AddField(
            model_name='answerchoice',
            name='test_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.testquestion'),
        ),
    ]