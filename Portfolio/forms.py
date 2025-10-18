from django import forms 
from .models import ContactMessage 
 
class ContactForm(forms.ModelForm): 
    class Meta: 
        model = ContactMessage 
        fields = ['name', 'email', 'subject', 'message'] 
        widgets = { 
            'name': forms.TextInput(attrs={ 
                'class': 'form-control', 
                'placeholder': 'Votre nom' 
            }), 
            'email': forms.EmailInput(attrs={ 
                'class': 'form-control', 
                'placeholder': 'Votre email' 
            }),  'subject': forms.TextInput(attrs={ 
                'class': 'form-control', 
                'placeholder': 'Sujet du message' 
            }), 
            'message': forms.Textarea(attrs={ 
                'class': 'form-control', 
                'placeholder': 'Votre message', 
                'rows': 5 
            }), 
        }