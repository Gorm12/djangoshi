from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'blog/blog_home.html')