
from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(req):
    posts = Post.objects.all()
    posts_desc = posts.order_by('-date')

    return render(req, 'posts/posts_list.html', {'posts': posts_desc})

def post_detail(req, slugzy):
    post = Post.objects.get(slug=slugzy)

    return render(req, 'posts/post_detail.html', {'post': post})