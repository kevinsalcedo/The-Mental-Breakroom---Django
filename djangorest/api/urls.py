from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, StoryCreateView, BlogPostCreateView
from .views import DetailsView, StoryDetailsView, BlogPostDetailsView

urlpatterns = {
        url(r'^disorders/$', CreateView.as_view(), name="create"),
        url(r'^disorders/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
        url(r'^stories/$', StoryCreateView.as_view(), name="create"),
        url(r'^stories/(?P<pk>[0-9]+)/$', StoryDetailsView.as_view(), name="details"),
        url(r'^blogposts/$', BlogPostCreateView.as_view(), name="create"),
        url(r'^blogposts/(?P<pk>[0-9]+)/$', BlogPostDetailsView.as_view(), name="details"),
        }
urlpatterns = format_suffix_patterns(urlpatterns)
