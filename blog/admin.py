from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author')







admin.site.register(Post, PostAdmin)
# Register your models here.

