from django.urls import path
from .views import SignInView, UserListView, UserDetailsView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/', UserDetailsView.as_view(), name='user_details'),
    path('users/', UserListView.as_view(), name='user_list'),
]
