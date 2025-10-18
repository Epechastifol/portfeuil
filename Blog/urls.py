from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name= "detail_article"),
]