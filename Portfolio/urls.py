from django.urls import path
from .views import *
from Core.views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('contact/', Contact_View, name= 'contact'),
    path('services-supplementaire/', Service_Supplementaire, name= 'services_supplementaire'),
    path('nos-services/', Services, name= 'services'),
    path('contacts-devis-personnalisé/', ContactsDevis, name= 'contacts_devis'),
    path('audit-&-evaluation/', Audit, name= 'audit'),
    path('audit-&-evaluation-competences/', Evaluation, name= 'evaluation'),
    path('Réalisations-&-cas-client/', Cas_Client, name= 'cas_client'),
    path('<int:pk>/updated/', UserUpdateView.as_view(), name='user_edite'),
    path('<int:pk>/view/', MessageDetailView.as_view(), name='message_read'),
]