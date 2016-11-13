from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(primary_key=True,max_length=20)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64, null=True)
    openid = models.CharField(max_length=100,unique=True)
    qq_num = models.CharField(max_length=30,unique=True)


class Sender(User):
    pass



class Taker(User):
    pass


class Order(models.Model):
    order_id = models.CharField(max_length=30,primary_key=True)
    original_file = models.FileField()