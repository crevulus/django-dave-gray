from django.shortcuts import render

# Create your views here.
def posts_list(req):
    return render(req, 'posts/posts_list.html')