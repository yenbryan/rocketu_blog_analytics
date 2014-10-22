from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'analytics.views.view_analytic', name='view_analytic'),
)