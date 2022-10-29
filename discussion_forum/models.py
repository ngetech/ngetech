from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ForumDiscussion(models.Model):
    title = models.CharField(max_length=50, default="")
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

class ForumReply(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    discussion = models.ForeignKey(ForumDiscussion, on_delete=models.CASCADE)
