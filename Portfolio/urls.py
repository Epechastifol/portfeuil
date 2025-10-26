from django.urls import path
from .views import *
from Core.views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('contenu-gratuit/', ContenuGratuit, name='contenu_gratuit'),
    path('nos-services/', Services, name= 'services'),
    path('consultances/', Consultances, name='consultances'),
    path('formations/', Formations, name='formations'),
    path('contacts-devis-personnalisé/', ContactsDevis, name= 'contacts_devis'),
    path('audit-&-evaluation-competences/', Evaluation, name= 'evaluation'),
    path('<int:pk>/updated/', UserUpdateView.as_view(), name='user_edite'),
    path('<int:pk>/view/', MessageDetailView.as_view(), name='message_read'),
]