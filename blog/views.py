from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render('blog/layout.html')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')