from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Coach(models.Model):
    uid = models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid', verbose_name='User Id')      
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    team = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
