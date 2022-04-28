from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdminConfig(admin.ModelAdmin):
    # readonly_fields = ["title"]
    list_filter = ['title']

admin.site.register(Post, PostAdminConfig)

