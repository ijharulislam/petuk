# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, phone, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not phone:
            raise ValueError('The field phone must be set')
        # email = self.normalize_email(email)
        user = self.model(phone=phone, is_active=True, is_staff=is_staff, is_superuser=is_superuser,
                          last_login=now,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        return self._create_user(phone, password, False, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        return self._create_user(phone, password, True, True, **extra_fields)
