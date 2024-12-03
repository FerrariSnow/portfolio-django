from datetime import date

from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'