from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser,PermissionsMixin):
    """custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255,default='a')
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email





    # username = None
    # email = models.EmailField(_('email address'), unique=True)
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    #
    # objects = CustomUserManager()
    #
    # def __str__(self):
    #     return self.email
