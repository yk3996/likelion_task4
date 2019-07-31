from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Portfolio
from django.utils import timezone
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def index(request):
    return render(request, 'index.html', {'index':index})