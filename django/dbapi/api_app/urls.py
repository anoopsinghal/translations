from django.urls import path
from .views import ArticleViews

urlpatterns = [
    path('save-translation', ArticleViews.as_view())
]