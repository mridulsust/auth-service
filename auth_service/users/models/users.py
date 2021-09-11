from django.contrib.auth.models import AbstractUser

from auth_service.common.models.base import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):
    """
    Custom User model that can be extended in the future if needed.

    Username and password are required. Other fields are optional.
    """
    pass
