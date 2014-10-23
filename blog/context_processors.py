import random
from blog.models import Post, Tag, Ad


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }


def list_tags(request):
    return {
        'all_tags': Tag.objects.filter(),
    }


def list_months(request):
    return {
        'posts': Post.objects.order_by('-created')
    }


def random_targeted_ad(request):
    # Get location of user and get random ad from its region
    # random_idx = random.randint(0, Ad.objects.count() - 1)
    return {
        'ad': ''
        # 'ad' : Ad.objects.filter(region=request.location['region'])[random_idx]
    }