from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Author, Category, Post
from django.http import HttpResponseBadRequest
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
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


class MarkdownPreviewView(TemplateResponseMixin, ContextMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            self.preview_data = data = request.POST['content']
        except KeyError:
            return HttpResponseBadRequest('No preview data specified.')

        return self.render_to_response(self.get_context_data(
            preview_data=data,
        ))


class BlogMarkdownPreviewView(MarkdownPreviewView):
    template_name = 'blog/preview.html'


def index(request):
    latest_post_list = Post.objects.filter(is_public=True).order_by('-created_on')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_public=True)
    return render(request, 'blog/detail.html', {'post': post})

def page(request, num):
    return HttpResponse(f'page {num}')