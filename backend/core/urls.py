from django.urls import path

from core import views

urlpatterns = [
    path('invitations/<int:pk>', views.InvitationRetrieveView.as_view(), name='invitation_retrieve'),
]
