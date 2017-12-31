from django.conf.urls import url, include
from django.contrib import admin
from companies import views
from rest_framework.urlpatterns import  format_suffix_patterns

urlpatterns = [
    url(r'^$', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url (r'^stocks/', views.StockList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)