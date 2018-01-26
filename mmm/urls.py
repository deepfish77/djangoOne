from django.conf.urls import url
from . import views
from mmm.views import PostListView, FilteredPosts

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
  url(r'^postdetails/$', PostListView.as_view(), name='postlistview'),
  
]

