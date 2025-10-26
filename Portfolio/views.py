from django.shortcuts import render, redirect
from .models import ContactMessage
from django.views.generic import DetailView
from django.contrib import messages 

def Home(request):
    return render(request, 'portfolio/home.html')


def Contact_View(request):  
    if request.method == 'POST':
        firstName = request.POST.get('firstName', '').strip()
        lastName = request.POST.get('lastName', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company = request.POST.get('company', '').strip()
        service = request.POST.get('service', '').strip()
        message_text = request.POST.get('message', '').strip()
        budget = request.POST.get('budget', '').strip() or None
        newsletter = True if request.POST.get('newsletter') == 'on' else False

        # Basic validation
        if not (firstName and lastName and email and service and message_text):
            messages.error(request, "Veuillez remplir les champs obligatoires.")
            return render(request, 'portfolio/contact_devis.html', {
                'firstName': firstName,
                'lastName': lastName,
                'email': email,
                'phone': phone,
                'company': company,
                'service': service,
                'message': message_text,
                'budget': budget,
                'newsletter': newsletter,
            })

        ContactMessage.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            phone=phone,
            company=company,
            service=service,
            message=message_text,
            budget=budget,
            newsletter=newsletter,
        )
        messages.success(request, "Merci ! Votre demande a bien été envoyée. Nous vous répondrons rapidement.")
        return redirect('home')

    return render(request, 'portfolio/contact_devis.html')


def ContenuGratuit(request):
    """Page listing free content/resources."""
    return render(request, 'portfolio/contenu_gratuit.html')


def Consultances(request):
    """Landing page for consultances with sections linking to Audit & Evaluation and Services complémentaires."""
    # we can include links/anchors to existing views 'audit' and 'services_supplementaire'
    return render(request, 'portfolio/consultances.html')


def Formations(request):
    """Page describing available formations."""
    return render(request, 'portfolio/formations.html')


class MessageDetailView(DetailView):
	model = ContactMessage
	template_name = 'admin/actions/detailsMessage.html'
	context_object_name = 'message'



def Evaluation(request):
    return render(request, 'portfolio/evaluation.html')

def Services(request):
    return render(request, 'portfolio/services.html')

def ContactsDevis(request):
    return render(request, 'portfolio/contacts_devis.html')

def Cas_Client(request):
    return render(request, 'portfolio/cas_client.html')
