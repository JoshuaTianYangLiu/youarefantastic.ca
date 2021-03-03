from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from .models import Author, Category, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)