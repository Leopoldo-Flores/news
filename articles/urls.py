from django.urls import path
from .views import Article

urlpatterns = [
    path('', ArticleListView.as_view(), name="article"),
    path('<int:pk>/detail', ArticleDetailView.as_view, name="article_detail")
    path('new/', ArticleListView.as_view(), name="article_create"),
    path('new/', ArticleCreateView.as_view(), name="article_update"),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name="article_delete"),
]