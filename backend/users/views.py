from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignInSerializer, UserSerializer

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password', 'old_password', 'new_password1', 'new_password2')
)

User = get_user_model()


class SignInView(GenericAPIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    serializer_class = SignInSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(SignInView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        user_logged_in.send(sender=user.__class__, request=request, user=user)

        return Response(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('role',)


class UserDetailsView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
