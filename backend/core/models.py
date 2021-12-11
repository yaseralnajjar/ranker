from datetime import date

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.db.models.aggregates import Max, Min
from django.utils.translation import gettext_lazy as _

from dateutil.relativedelta import relativedelta

User = get_user_model()


class General:
    pass


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Types of questions:
    - one-choice: a question with only one valid answer
    - multi_choice: a question with multiple valid answers
    - fill-in-blanks: a question that has no right or wrong answer
    - code: a question that is answered using code
    """

    TYPE_CHOICES = (
        ('one_choice', 'one-choice'),
        ('multi_choice', 'multi-choice'),
        # ('fill_in_blanks', 'fill-in-blanks'),
        # ('code', 'code'),
    )

    tag = models.ForeignKey(Tag, related_name='questions', on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    score = models.IntegerField(default=5)
    # time_limit_mins = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.description


class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, null=False)

    description = models.TextField(max_length=1000)
    is_correct = models.BooleanField(default=False)


class Test(models.Model):
    questions = models.ManyToManyField('Question', through='TestQuestion', through_fields=('test', 'question'))

    name = models.CharField(max_length=300)
    time_limit_mins = models.IntegerField()
    is_randomized = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    order = models.PositiveIntegerField(default=0)

    models.UniqueConstraint(fields=['test', 'question', 'order'], name='unique_test_question')

    @classmethod
    def reorder_test_questions(cls, test):
        """Reorder all test questions starting from 0 until last question count"""
        test_question_ids = list(cls.objects.filter(test=test).order_by('order').values_list('pk', flat=True))

        print(test_question_ids)

        with transaction.atomic():
            current_order = 0
            for test_question_id in test_question_ids:
                print(
                    test_question_id,
                    current_order,
                    cls.objects.filter(pk=test_question_id).first().question.description,
                )
                cls.objects.filter(pk=test_question_id).update(order=current_order)
                current_order += 1

    def save(self):
        super().save()
        self.__class__.reorder_test_questions(test=self.test)

    class Meta:
        ordering = ('order',)
        # ordering = ('test__id', 'order')

    def __str__(self):
        return self.question.description


class AnswerChoice(models.Model):
    test_question = models.ForeignKey(TestQuestion, related_name='answers', on_delete=models.CASCADE)
    chosen_answer = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, related_name='chosen_answers', on_delete=models.CASCADE)

    models.UniqueConstraint(fields=['test_question', 'chosen_answer', 'candidate'], name='unique_answer_choice')
    # data = models.TextField(max_length=1000)

    class Meta:
        ordering = ('candidate', 'test_question__id')

    def __str__(self):
        return f'{self.candidate.id} {self.test_question.id}'


class Invitation(models.Model):
    created_by = models.ForeignKey(User, related_name='invitations', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='invitations', on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.test.name

    def invalidate(self):
        self.is_valid = False
        self.save()


class Submission(models.Model):
    invitation = models.OneToOneField(Invitation, on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey(Test, related_name='submissions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)

    is_submitted = models.BooleanField(default=False)
    questions_and_answers = models.JSONField(null=True)
    total_score = models.IntegerField(default=0)
    tag_scores = models.JSONField(null=True)
    time_started = models.DateTimeField(auto_now_add=True)
    time_finished = models.DateTimeField(auto_now=True)

    @property
    def time_elapsed(self):
        return relativedelta(self.time_finished, self.time_started)

    def calculate_score(self):
        pass

    def compose_questions_and_answers(self):
        pass

    def compose_tag_scores(self):
        pass

    def clean(self):
        if self.is_submitted:
            raise ValidationError(_('Cannot make changes after submission!'))

        super().clean()

    def save(self, *args, **kwargs):
        # is_time_finished = self.time_elapsed >= self.test.time_limit_mins
        print(self.time_elapsed)
        # if is_time_finished:
        #    print('hey')
        #    self.score = self.calculate_score()
        #    self.questions_and_answers = self.compose_questions_and_answers()
        #    self.tag_scores = self.compose_tag_scores()
        #    self.is_submitted = True
        #    super().save(*args, **kwargs)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('total_score',)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
