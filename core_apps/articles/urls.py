from django.urls import path

from .views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView

urlpatterns = [
    path("", ArticleListCreateView.as_view(), name="articles-list-create"),
    path("<uuid:id>/", ArticleRetrieveUpdateDestroyView.as_view(), name="article-retrieve-update-destroy"),
]
