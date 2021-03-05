from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from martor.models import MartorField
from .models import Author, Category, Post
from django.urls import reverse_lazy
# Register your models here.

class NewAdminMartorWidget(AdminMartorWidget):
    class Media:
        # css = {
        #     'all': ['']
        # }
        js = ['admin/js/jquery.init.js', 'blog/martor-mathjax.js']

class PostAdmin(admin.ModelAdmin):
    model = Post
    formfield_overrides = {
        MartorField: {'widget': NewAdminMartorWidget(attrs={'data-markdownfy-url': reverse_lazy('blog_preview'),})},
        models.TextField: {'widget': NewAdminMartorWidget(attrs={'data-markdownfy-url': reverse_lazy('blog_preview'),})},
    }
    autocomplete_fields = ('categories','authors',)

    class Media:
        css = {
            "all": ("blog/admin-widget.css",)
        }
        js = ("blog/martor-mathjax.js",)

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)