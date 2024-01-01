from django.urls import path

from .views import ResponseListCreateView, ResponseUpdateDestroyView

urlpatterns = [
    path(
        "article/<uuid:article_id>/",
        ResponseListCreateView.as_view(),
        name="article_responses",
    ),
    path("<uuid:id>/", ResponseUpdateDestroyView.as_view(), name="response_detail"),
]
