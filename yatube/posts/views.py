from django.shortcuts import render, get_object_or_404

from .models import Post, Group


count_posts = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:count_posts]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
