from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

# blog/
# blog/:id/
# blog/page/:id/
# Allow commenting?
# Support markdown + mathjax
# Title, author, date (created_on, last_modified), body, categories (tags), image

# Add later support for
# commenting (anonymous, add filter to keep messages safe)
# filters

def index(request):
    return HttpResponse('<h1>Not Implemented Yet!</h1>')

def detail(request, pk):
    return HttpResponse(f'detail {pk}')

def page(request, num):
    return HttpResponse(f'page {num}')