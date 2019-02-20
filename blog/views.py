from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Zayar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 19, 2019'
    },
    {
        'author': 'Zayar',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 19, 2019'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')