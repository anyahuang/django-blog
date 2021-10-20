from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def home(request):
    blog_posts = Blog.objects.all()
    context = {"blog_post":blog_post}
    return render(request,"blog/home.html",context)

def blog_post(request, id):
    blog_post = Blog.objects.get(id=id)
    context = {"blog":blog }
    return render(request, "blog/blog_post.html",context)
    