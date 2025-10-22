from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class ContactMessage(models.Model): 
    firstName = models.CharField(max_length=100, verbose_name="Nom") 
    lastName = models.CharField(max_length=100, verbose_name="Prénom") 
    email = models.EmailField(verbose_name="Email") 
    phone = models.CharField(max_length=100, verbose_name="Téléphone")
    company = models.CharField(max_length=100, verbose_name="Entréprise / Organisation")
    service = models.CharField(max_length=200, verbose_name="Services souhaité") 
    message = models.TextField(verbose_name="Message") 
    budget = models.CharField(max_length=120, verbose_name="Budget Prévisionnel", blank= True, null=True) 
    newsletter = models.BooleanField(default= False)
    is_read = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi") 
     
    class Meta: 
        verbose_name = "Message de contact" 
        verbose_name_plural = "Messages de contact" 
     
    def __str__(self): 
        return f"{self.firstName} {self.lastName} - {self.email}" 