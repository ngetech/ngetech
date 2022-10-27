from django.db import models
from django.contrib.auth.models import User
from post_tech.models import PostTech

# Create your models here.
class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    post = models.ForeignKey(PostTech, on_delete=models.CASCADE)
    comment = models.TextField()