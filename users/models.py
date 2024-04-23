from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Failed to set email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if 'name' not in extra_fields or 'last_name' not in extra_fields:
            raise ValueError('Superuser must have a name and a last name.')
    
        # Asegurar que el género está siendo especificado
        if 'gender' not in extra_fields:
            raise ValueError('Superuser must have a gender specified.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    GENDER_CHOICES = (
        (0, 'Man'),
        (1, 'Female'),
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    phone = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'gender']
    
USER_FIELDS = 'email'

class Patient(User):
    no_dpi = models.CharField(max_length=20)

class Doctor(User):
    speciality = models.JSONField(default=list)
    no_collegiate = models.CharField(max_length=20)


