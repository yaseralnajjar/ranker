from datetime import date
from django.db import models
from django_jsonfield_backport.models import JSONField
from django.contrib.auth import get_user_model


User = get_user_model()


class General(models.Model):
    pass


class Test(models.Model):
    name = models.CharField(max_length=300)
    time_limit_mins = models.IntegerField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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

    description = models.TextField(max_length=1000)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    total_mark = models.IntegerField(default=5)
    time_limit_mins = models.IntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.description


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    users_chosen = models.ManyToManyField(
        User, related_name='chosen_answers', blank=True)

    description = models.TextField(max_length=1000)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.description


class Submission(models.Model):
    test = models.ForeignKey(
        Test, related_name='submissions', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='submissions', on_delete=models.CASCADE)

    is_submitted = models.BooleanField(default=False)
    score = models.IntegerField()
    time_started = models.DateTimeField(auto_now_add=True)
    time_finished = models.DateTimeField(auto_now=True)
    time_elapsed = models.DateTimeField()

    def calculate_score(self):
        pass

    def save(self, *args, **kwargs):
        if is_submitted:
            raise ValidationError('Cannot make changes after submission!')
        else:
            self.time_elapsed = self.time_finished - self.time_started
            self.score = self.calculate_score()
            super().save(*args, **kwargs)

    class Meta:
        ordering = ('score', )

    def __str__(self):
        return self.user
