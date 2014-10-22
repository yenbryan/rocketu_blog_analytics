from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from rocketu_blog_analytics import settings

urlpatterns = patterns('',

    url(r'^', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', include('analytics.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)