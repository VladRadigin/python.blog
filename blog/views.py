from django.shortcuts import render
from .models import Post

class BlogView:
    model = Post
    template_name = 'blog.html'