from rest_framework import serializers, exceptions

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        try:
            return self._choices[obj]
        except KeyError:
            return obj


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                raise exceptions.ValidationError(_('User account is disabled.'))

            if user.role == 'itm' or user.role == 'other':
                raise exceptions.ValidationError(_('Unable to log in with provided credentials.'))

        else:
            raise exceptions.ValidationError(_('Unable to log in with provided credentials.'))

        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    role = CustomChoiceField(User.ROLES_CHOICES)

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'role', 'position')
