from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView

from .serializers import UserSerializer

User = get_user_model()


class UserDetailView(RetrieveAPIView):
    """
    Updates and retrieves user accounts
    """
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
