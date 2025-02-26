from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'media_type']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
# Compare this snippet from posts/views.py:     
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Post  # Import Post model
# from .forms import PostForm  # Import PostForm