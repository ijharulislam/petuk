from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(unique=True, max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural ='users'

    def __str__(self):
        if self.email:
            return u"Email: {}".format(self.email)
        return u"Phone: {}".format(self.phone)

    def get_short_name(self):
        return u"{}".format(self.full_name)