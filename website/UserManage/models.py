from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(primary_key=True,max_length=20)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64, null=True)
    openid = models.CharField(max_length=100,unique=True)