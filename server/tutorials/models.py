from django.db import models
from django.contrib.postgres.fields import ArrayField


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)


class User(models.Model):
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=20, default='')
    balance = models.IntegerField()
    transactions = ArrayField(models.CharField(max_length=100), default=list())
