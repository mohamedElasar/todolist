from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

from django.conf import settings


class CustomUser(AbstractBaseUser,PermissionsMixin):
    """custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique = True)
    username = models.CharField(max_length=255,default='a')
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email


class Tag(models.Model):
    """tag to be used for to do list """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,

    )
    def __str__(self):
        return self.name





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
