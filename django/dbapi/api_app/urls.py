from django.urls import path
from .views import ArticleViews

urlpatterns = [
    path('saveTranslation/', ArticleViews.as_view())
]