from enum import Enum

from django.contrib.auth.models import AbstractUser, Permission
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPER_USER = 1, _('Super User')
        RECRUITER = 2, _('Recruiter')
        TEST_TAKER = 3, _('Test Taker')
        OTHER = 4, _('Other')

    email = models.EmailField('email address', unique=True)
    role = models.CharField(choices=Roles.choices, default=Roles.OTHER, max_length=64)

    def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'
