from django.db import models

# Create your models here.
# Allow commenting?
# Support markdown + mathjax
# Title, author, date (created_on, last_modified), body, categories (tags), image

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    authors = models.ManyToManyField('Author', related_name='posts')
    image = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title
    