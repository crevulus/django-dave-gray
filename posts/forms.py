from django import forms
from . import models # . = current directory

class CreatePost(forms.ModelForm):
  class Meta: # must be named Meta
    model = models.Post
    fields = ['title', 'body', 'slug', 'image']