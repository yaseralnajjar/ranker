from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.core.exceptions import ValidationError


class User(AbstractUser):

    SUPER_USER = 'spr'
    RECRUITER = 'recr'
    TEST_TAKER = 'tst'
    OTHER = 'other'

    ROLES_CHOICES = (
        (SUPER_USER, 'Super User'),
        (RECRUITER, 'Recruiter'),
        (TEST_TAKER, 'Test Taker'),
        (OTHER, 'Other'),
    )

    email = models.EmailField('email address', unique=True)
    role = models.CharField(choices=ROLES_CHOICES,
                            default='Other', max_length=64)

    def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'
