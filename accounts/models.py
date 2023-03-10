from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_master = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Master(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)

    def __str__(self):
        return self.user

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    mark = models.IntegerField

    def __str__(self):
        return self.user

class Calculation(models.Model):
    expression = models.CharField(max_length=200)
    result = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.expression