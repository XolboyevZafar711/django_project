from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserList(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    objects = None
    list_name = models.ForeignKey(UserList, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_done = models.BooleanField()

    def __str__(self):
        return self.name


