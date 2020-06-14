from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Game(models.Model):
    gamers_name = models.CharField(max_length=50)
    gamers_password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gamers_name
