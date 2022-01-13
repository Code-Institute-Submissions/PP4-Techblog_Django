from django.contrib import admin
from .models import Post, Category, UserProfile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)

# Register your models here.
