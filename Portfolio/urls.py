from django.urls import path
from .views import *
from Core.views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('contact/', Contact_View, name= 'contact'),
    path('services-supplementaire/', Services, name= 'services'),
    path('audit-&-evaluation/', Audit, name= 'audit'),
    path('audit-&-evaluation-competences/', Evaluation, name= 'evaluation'),
    path('<int:pk>/updated/', UserUpdateView.as_view(), name='user_edite'),
    path('<int:pk>/view/', MessageDetailView.as_view(), name='message_read'),
]