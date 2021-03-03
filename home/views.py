from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from django.contrib.staticfiles.views import serve



# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def projects(request):
    return render(request, 'home/projects.html')

def resume(request):
    return serve(request, 'home/resume.pdf')
