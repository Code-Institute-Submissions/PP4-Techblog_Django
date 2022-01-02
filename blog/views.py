from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostingForm, EditForm
from django.urls import reverse_lazy


# def home(request):
# return render(request, 'home.html', {})


class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-publication_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostingForm
    template_name = 'add_post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
