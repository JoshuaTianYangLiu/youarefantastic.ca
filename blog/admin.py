from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from .models import Author, Category, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    autocomplete_fields = ('categories','authors',)

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)