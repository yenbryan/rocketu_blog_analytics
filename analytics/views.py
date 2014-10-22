from django.db.models import Count
from django.shortcuts import render
from analytics.models import Page, View


def view_analytic(request):
    pages = Page.objects.all()
    page_views = View.objects.filter(page=pages)
    page_view_counts = page_views.values('page').annotate(number_of_views=Count('page'))

    data = {
        'pages': pages,
        'page_views': page_views,
        'page_view_counts': page_view_counts,
    }
    return render(request,'analytic/view_analytic.html', data)