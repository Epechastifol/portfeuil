from django.shortcuts import render
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView

# Create your views here.

class ArticleDetailView(DetailView):
	model = Articles
	template_name = 'admin/actions/detailsArticle.html'
	context_object_name = 'article'
