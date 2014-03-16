from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class HomeView(ListView):
    model = Post
    paginate_by = 20

class PostDetailView(DetailView):
    model = Post
    slug_field = 'pk'
