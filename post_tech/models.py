from django.db import models
from django.contrib.auth.models import User

class PostTech(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )
    username = models.CharField(
        max_length=50,
        blank=True, 
        null=True,
    )
    title = models.CharField(
        max_length=160
    )
    description = models.TextField()
    date = models.DateField(
        auto_now=True
    )