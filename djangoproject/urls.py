from django.conf.urls import url, include 
from django.contrib import admin
from companies import views as companyviews
from rest_framework import routers
from restone import views as restViews
from snippets import views as snippetviews
from django.urls.conf import path


#rest Url Patterns
router = routers.DefaultRouter()
router.register(r'users', restViews.UserViewSet)
router.register(r'groups', restViews.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^stocks/', companyviews.StockList.as_view()),
    url(r'^snippets/$', snippetviews.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippetviews.SnippetDetail.as_view()),
    path('accounts/', include('django.contrib.auth.urls'))

    
]

   
#urlpatterns = format_suffix_patterns(urlpatterns)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# company url patterns




