from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.views import View, generic

from blogapp.models import Post


def login_required_decorator(func):
    return login_required(func, login_url='blog:login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('blog:login_page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:home_page')
    return render(request, 'login.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:login_page')
    template_name = 'registration.html'


@login_required_decorator
def home_page(request):
    queryset = Post.published.all()
    context = {
        'posts': queryset
    }

    return render(request, 'index.html', context=context)


@login_required_decorator
def post_detail_page(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'detail.html', {'post': post})
