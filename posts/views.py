from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Create your views here.

# Homepage (Global Feed)
@login_required
def home(request):
    posts = Post.objects.all()
    
    # Filtering Logic
    user_filter = request.GET.get('user')
    media_filter = request.GET.get('media_type')
    sort_by = request.GET.get('sort', 'newest')

    if user_filter:
        posts = posts.filter(author__username=user_filter)

    if media_filter:
        posts = posts.filter(media_type=media_filter)

    if sort_by == 'oldest':
        posts = posts.order_by('created_at')

    return render(request, 'posts/home.html', {'posts': posts})


# Profile Page
@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)

    media_filter = request.GET.get('media_type')
    sort_by = request.GET.get('sort', 'newest')

    if media_filter:
        posts = posts.filter(media_type=media_filter)

    if sort_by == 'oldest':
        posts = posts.order_by('created_at')

    return render(request, 'posts/profile.html', {'posts': posts})


# Create Post
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})

# Edit Post
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

# Delete Post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == "POST":
        post.delete()
        return redirect('profile')

    return render(request, 'posts/delete_post.html', {'post': post})
# Compare this snippet from social_media/urls.py:
# from django.contrib import admin
