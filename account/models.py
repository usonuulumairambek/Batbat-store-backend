from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
import hashlib


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, first_name, last_name, phone_num, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.phone_num = phone_num

        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    type_of_profile = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    bonus = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    is_active = models.BooleanField(
        default=False,
        help_text='Код активации активирован - True, нет - False')
    activation_code = models.CharField(max_length=100, blank=True)
    favorites = models.ManyToManyField("Shope.Product", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Генерация активационного кода
    def create_activation_code(self):
        string = self.email + str(self.id)
        encode_string = string.encode()
        md5_object = hashlib.md5(encode_string)
        activation_code = md5_object.hexdigest()
        self.activation_code = activation_code


