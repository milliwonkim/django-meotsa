from django.shortcuts import render, redirect
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
def read_blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    # blog_list.html의 '?page=1'의 page를 의미
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog_list.html', {'posts': posts})

def blog_new(request):
    return render(request, 'blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.save()
    return redirect('read_blog_list')
    # blogs = Blog.objects.all()
    # return render(request, 'blog_list.html', { 'blogs': blogs })

# 여기에 있는 blog_id와 urls.py 의 int:blog_id가 같아야함
def read_blog_one(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog_detail.html', {'blog':blog})

def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.save()
    return redirect('read_blog_list')

def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    # 'read_blog_list' 함수를 말하는거임 여기안에있는거
    return redirect('read_blog_list')