from datetime import date
from dateutil.relativedelta import relativedelta
from copy import copy
from django.db import models
from django_jsonfield_backport.models import JSONField
from django.contrib.auth import get_user_model


User = get_user_model()


class General(models.Model):
    pass


class Test(models.Model):
    name = models.CharField(max_length=300)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    TYPE_CHOICES = (
        ('one_choice', 'one-choice'),
        ('multi_choice', 'multi-choice'),
        ('code', 'code'),
    )

    test = models.ForeignKey(
        Test, related_name='questions', on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, related_name='questions',
                            on_delete=models.SET_NULL, null=True)

    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    users_chosen = models.ManyToManyField(User, related_name='chosen_answers')

    description = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)
