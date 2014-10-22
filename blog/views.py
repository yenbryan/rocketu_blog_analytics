import random
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from blog.models import Post, Tag


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })


def view_tag(request, tag_name):

    return render(request,'view_tag.html',{
        'posts': Post.objects.filter(tags__name=tag_name),
        'tag': tag_name
    })