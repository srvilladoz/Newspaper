from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ["title", "body", "image", "author"]

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body", "image"]

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")
