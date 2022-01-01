from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=150, default="Mark Techblog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

# Create your models here.
