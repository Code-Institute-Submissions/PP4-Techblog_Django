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

# The model for the Userprofile object

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


# The Model for a Blog Post, using PK for post entry in DB


class Post(models.Model):
    title = models.CharField(max_length=50)
    head_img = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=150)
    snip = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
