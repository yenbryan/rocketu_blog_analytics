from blog.models import Post


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }