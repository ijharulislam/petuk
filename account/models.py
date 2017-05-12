from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserProfileManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=20, default='', blank=True, null=True)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return u"Email: {}".format(self.email)

    def get_full_name(self):
        """ Returns the full name """
        name = u"{} {}".format(self.first_name, self.last_name)
        return name.strip()

    def get_short_name(self):
        return u"{}".format(self.email)