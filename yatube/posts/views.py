from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Post, Group, User
from .forms import PostForm


COUNT_POSTS: int = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, COUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:COUNT_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts_count = author.posts.count()
    posts = Post.objects.filter(author=author)
    paginator = Paginator(posts, COUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/profile.html'

    context = {
        'author': author,
        'posts_count': posts_count,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    all_authors_posts = Post.objects.select_related('author').all()
    post_count = 0
    for post in all_authors_posts:
        if post.id == post_id:
            author_of_post = post.author.username
    for post in all_authors_posts:
        if post.author.username == author_of_post:
            post_count += 1
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post_count': post_count,
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', username=request.user.username)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    form = PostForm(request.POST or None)
    post = Post.objects.get(id=post_id)
    author = post.author.username
    if author != request.user.username:
        return redirect('posts:post_detail', post.id)
    if form.is_valid():
        post.text = form.cleaned_data['text']
        post.save()
        return redirect('posts:post_detail', post.id)
    context = {
        'form': form,
        'is_edit': True,
        'post': post}
    return render(request, 'posts/create_post.html', context)
