from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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
        'posts': Post.objects.all()
    }
    return render(request, 'ikariam/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'ikariam/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'ikariam/about.html', {'title': 'About'})
