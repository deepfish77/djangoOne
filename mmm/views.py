from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.views.generic.list import ListView


def index(request):
 

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
        }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
  }


    return render(request, 'posts/details.html', context)

def posts_view(request):
    template_name = 'posts/details.html'
    queryset = Posts.objects.all()
    context = { 
        "object_list": queryset
        }
    return render(request,template_name,context)

class PostListView(ListView):
  
    queryset = Posts.objects.all()
    print(queryset)
    template_name = 'posts/details.html'
    
    
class FilteredPosts(ListView):
    queryset = Posts.objects.count()
    