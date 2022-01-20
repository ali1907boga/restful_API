from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Article

class ArticlelIST(ListView):

    template_name = 'home.html'
    def get_queryset(self):
        return Article.objects.all()

class ArticleDetail(DetailView):

    template_name = 'detail.html'
    def get_object(self):
        return get_object_or_404(Article,pk = self.kwargs.get('pk'))
