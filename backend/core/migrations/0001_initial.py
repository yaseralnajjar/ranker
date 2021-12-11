# Generated by Django 3.2.10 on 2021-12-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ('candidate__id', 'test_question__id'),
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('type', models.CharField(choices=[('one_choice', 'one-choice'), ('multi_choice', 'multi-choice')], max_length=20)),
                ('score', models.IntegerField(default=5)),
                ('time_limit_mins', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('time_limit_mins', models.IntegerField()),
                ('is_randomized', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=1)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.test')),
            ],
            options={
                'ordering': ('test__id', 'order'),
            },
        ),
        migrations.AddField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(through='core.TestQuestion', to='core.Question'),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_submitted', models.BooleanField(default=False)),
                ('questions_and_answers', models.JSONField(null=True)),
                ('total_score', models.IntegerField(default=0)),
                ('tag_scores', models.JSONField(null=True)),
                ('time_started', models.DateTimeField(auto_now_add=True)),
                ('time_finished', models.DateTimeField(auto_now=True)),
                ('invitation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.invitation')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='core.test')),
            ],
            options={
                'ordering': ('total_score',),
            },
        ),
    ]
