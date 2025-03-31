from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('create-post/', views.post_create, name="create-post"),
    path('<slug:slugzy>/', views.post_detail, name='post-detail') # dynamic URLs below static URLs
]