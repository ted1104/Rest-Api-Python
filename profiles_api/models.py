from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile (AbstractBaseUser, PermissionsMixin):
    """Databse model for users in the system"""

    email.models.EmailField(max_length=254, unique=True)
    name.models.CharField(max_length=254)
    is_active.models.BooleanField(default=True)
    is_staff.models.BooleanField(default=False)

    objects = UserProfileManage()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve shot name of user"""
        return self.name

    def __str__(self):
        """Return string represnetation for our user"""
        return self.email


# Create your models here.
