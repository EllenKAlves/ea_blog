from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts, 
    }
    return render(request, "blog/index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context ={
        "post": post,
        "comments": comments,
    }
    return render(request, "blog/detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(category__name=category)
    context ={
        "posts": posts,
        "category": category,
    }
    return render(request, "blog/category.html", {"posts": posts, "category": category})


    