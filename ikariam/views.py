from django.shortcuts import render

posts = [
    {
        'author': 'Joe Doe',
        'title': 'Some Content',
        'content': 'First  content',
        'date_posted': 'July 14, 2020'
    },
    {
        'author': 'Joe Doe',
        'title': 'Post 2',
        'content': 'Second post ',
        'date_posted': 'June 14, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'ikariam/home.html', context)


def about(request):
    return render(request, 'ikariam/about.html', {'title': 'About'})
