# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, is_staff, is_superuser, **extra_fields):
        email = extra_fields["email"]
        print("Email from manager", email)
        if email:
            email = self.normalize_email(email)
            extra_fields["email"] = email
        user = self.model(is_staff=is_staff, is_active=True, is_superuser=is_superuser, **extra_fields)
        password = extra_fields["password"]
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        return self._create_user(False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)