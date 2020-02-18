import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CognitoUserManager


class User(AbstractUser):

    cognito_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects = CognitoUserManager()
