from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm
from django.views.generic import DetailView
from django.contrib import messages 

def Home(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            # Sauvegarde automatique dans la base de données 
            form.save() 
            # Message de succès 
            messages.success(request, 'Votre message a été envoyé avec succès !') 
            return redirect('home') 
    else: 
        form = ContactForm() 

    context = {
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)


def Contact_View(request): 
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            # Sauvegarde automatique dans la base de données 
            form.save() 
            # Message de succès 
            messages.success(request, 'Votre message a été envoyé avec succès !') 
            return redirect('home') 
    else: 
        form = ContactForm() 
     
    return render(request, 'portfolio/contact.html', {'form': form})


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