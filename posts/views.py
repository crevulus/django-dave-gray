
from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy # need to use reverse_lazy to prevent being evaluated immediately, which would lead django to try to resolve url before it's finished loading all URL patterns = circular import

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    posts_desc = posts.order_by('-date')

    return render(request, 'posts/posts_list.html', {'posts': posts_desc})

def post_detail(request, slugzy):
    post = Post.objects.get(slug=slugzy)

    return render(request, 'posts/post_detail.html', {'post': post})

# decorator acts like HOC/hook
@login_required(login_url=reverse_lazy('users:login')) 
def post_create(request):
    return render(request, 'posts/post_create.html')