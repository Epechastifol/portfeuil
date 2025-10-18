from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, ContactMessage
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView
from django.contrib import messages 

def Home(request):
    projects = Project.objects.all().order_by('-date_completed')

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
        'projects': projects,
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug= slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})


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
