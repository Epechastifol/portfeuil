from django.shortcuts import render, redirect
from .models import ContactMessage
from django.views.generic import DetailView
from django.contrib import messages 

def Home(request):
    return render(request, 'portfolio/home.html')


def Contact_View(request):  
     
    return render(request, 'portfolio/contact.html')


class MessageDetailView(DetailView):
	model = ContactMessage
	template_name = 'admin/actions/detailsMessage.html'
	context_object_name = 'message'


def Audit(request):
    return render(request, 'portfolio/audit.html')

def Evaluation(request):
    return render(request, 'portfolio/evaluation.html')

def Services(request):
    return render(request, 'portfolio/services.html')

def ContactsDevis(request):
    return render(request, 'portfolio/contacts_devis.html')

def Cas_Client(request):
    return render(request, 'portfolio/cas_client.html')

def Service_Supplementaire(request):
    return render(request, 'portfolio/services_sup.html')