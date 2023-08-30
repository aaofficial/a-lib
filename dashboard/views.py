
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from home.models import Post



@login_required
def menu_view(request):
    return render(request, 'main.html')

@login_required
def add_view(request):
    submitted = False  # Initialize a flag to indicate successful submission

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            submitted = True  # Set the flag after successful submission
    else:
        form = PostForm()

    context = {'form': form, 'submitted': submitted}  # Pass the flag to the template
    return render(request, 'addp.html', context)

@login_required
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')
    return render(request, 'delete_post.html', {'post': post})