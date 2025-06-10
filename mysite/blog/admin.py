from django.contrib import admin
from .models import Post
from .models import Members
from .models import Category, Image


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'isActive','Category')
    search_fields = ('title', 'content', 'author', 'tags')
    list_filter = ('date', 'isActive')  
    ordering = ('-date',)

admin.site.register(Post, PostAdmin)

class MembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)

admin.site.register(Members, MembersAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)
admin.site.register(Category, CategoryAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url',)
    search_fields = ('image_url',)
    ordering = ('image_url',)
admin.site.register(Image, ImageAdmin)

from .models import Viewers
class ViewersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    ordering = ('name',)

admin.site.register(Viewers, ViewersAdmin)
