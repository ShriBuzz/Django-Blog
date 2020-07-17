from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import CreateView
from .forms import PostModelForm


def home_view(request):
    return render(request, 'home.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    form_class = PostModelForm
    template_name = 'create.html'
    success_url = '/blog'
