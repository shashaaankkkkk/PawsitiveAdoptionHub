# backends.py in the 'user' app

from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class RoleBasedBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
