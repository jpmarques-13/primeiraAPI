from .views import BlogPostRudViews, BlogPostAPIViews
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudViews.as_view(), name='post-rud'),
    url(r'^$', BlogPostAPIViews.as_view(), name='post-create'),
]
