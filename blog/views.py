from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')
