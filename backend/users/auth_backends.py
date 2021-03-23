from django.contrib.auth.backends import ModelBackend

from .models import User


class AuthenticationBackend(ModelBackend):

    def authenticate(self, request, **credentials):
        email_address = credentials.get('email')

        if email_address is None:
            email_address = credentials.get('username')

        password = credentials.get('password')

        if email_address is None:
            return None

        try:
            user = User.objects.get(email=email_address)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
            return None
