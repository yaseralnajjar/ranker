from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import Invitation, Submission, Test

User = get_user_model()


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
