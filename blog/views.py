from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Marcin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August, 27, 2018'
    },
    {
        'author': 'Bartek',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August, 28, 2018'
    },
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)    #blog/home - pobrany z templateów, context - wyslany do templateów
#    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
