from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManage(BaseUserManager):
    """Manage for user profile"""

    def create_user(self, email, name, password=None):
        """create a new profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, name, password):
        """create and save a new super user with given details"""
        user = self.create_user(email, password, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)


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
