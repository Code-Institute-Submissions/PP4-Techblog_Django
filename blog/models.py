from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(null=True, blank=True, upload_to="images/avatar/")

    website_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=50)
    head_img = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=150, default='uncategorised')
    snip = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    
    def get_absolute_url(self):
        return reverse('home')
