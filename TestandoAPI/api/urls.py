from .views import BlogPostRudViews
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudViews.as_view(), name='post-rud')
]
