from django.shortcuts import render, redirect

from .forms import PostCreateForm
from .models import Post

def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            photo = form.cleaned_data.get('photo')
            content = form.cleaned_data.get('content')
            post = Post.objects.create(title=title, photo=photo, content=content)
            return redirect('post_detail', post_pk=post.pk)
    else:
        form = PostCreateForm

    context = {
        'form': form
    }
    return render(request, 'post/post_create.html', context)


