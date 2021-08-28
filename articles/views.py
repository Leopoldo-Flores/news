from django.views.generic import ListView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = Article  
    template_name = 'article_list.html'

class ArticleDetailView(DeteailView):
    model = Article
    template_name = 'article_detail.html'
    
class ArticleCreateView(createview):
    model = Article
    template_name = 'article_new.html;
    fields = ['title', 'body']

class ArticleDeleteView(deleteView):
    model = Article 
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles')




