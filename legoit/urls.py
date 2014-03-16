from django.conf.urls import patterns, include, url
from django.contrib import admin

from posts.views import HomeView, PostDetailView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
