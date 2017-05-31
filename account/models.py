from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(unique=True, max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural ='users'

    def __str__(self):
        if self.email:
            return u"Email: {}".format(self.email)
        return u"Phone: {}".format(self.phone)

    @property
    def is_staff(self):
        return self.is_admin