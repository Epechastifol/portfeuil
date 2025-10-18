from django.urls import path
from .views import *
from Core.views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('projet/<slug:slug>/', project_detail, name= 'project_detail'),
    path('contact/', Contact_View, name= 'contact'),
    path('<int:pk>/updated/', UserUpdateView.as_view(), name='user_edite'),
    path('<int:pk>/view/', MessageDetailView.as_view(), name='message_read'),
]