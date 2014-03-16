from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class HomeView(ListView):
    model = Post
    template_name = "posts/post_list.jinja"
    paginate_by = 20

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.jinja"
    slug_field = 'pk'
