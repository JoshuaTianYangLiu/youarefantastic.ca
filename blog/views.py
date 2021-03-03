from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Author, Category, Post
# Create your views here.

# blog/?page=1
# blog/:id/
# blog/page/:id/
# Allow commenting?
# Support markdown + mathjax
# Title, author, date (created_on, last_modified), body, categories (tags), image

# Add later support for
# commenting (anonymous, add filter to keep messages safe)
# filters

def index(request):
    latest_post_list = Post.objects.order_by('-created_on')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return HttpResponse(f'detail {post.body}')

def page(request, num):
    return HttpResponse(f'page {num}')