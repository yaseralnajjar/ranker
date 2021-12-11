from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import Invitation, Submission
from .serializers import InvitationSerializer


class InvitationRetrieveView(RetrieveAPIView):
    serializer_class = InvitationSerializer
    queryset = Invitation.objects
