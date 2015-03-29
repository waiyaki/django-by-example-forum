from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_forum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('forum.urls')), # No namespace here.
    url(r'^forum/', include('forum.urls', namespace='forum')),
    url(r'^admin/', include(admin.site.urls)),
)
