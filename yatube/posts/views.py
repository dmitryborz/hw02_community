from django.shortcuts import render, get_object_or_404

from .models import Post, Group


COUNT_POSTS: int = 10


def index(request):
    posts = Post.objects.all()[:COUNT_POSTS]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
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
