
from django.contrib import admin 
from django.contrib.messages.views import SuccessMessageMixin
from django.template.response import TemplateResponse 
from django.urls import path 
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.db.models import Count 
from Portfolio.models import *
from Blog.models import *
from .views import *


class CustomAdminSite(admin.AdminSite): 
    site_header = "Administration Portfolio" 
    site_title = "Portfolio Admin" 
    index_title = "Tableau de bord" 
     
    
    def custom_stats_view(self, request): 
        # Vos statistiques personnalisées 
        context = { 
            'title': 'Statistiques avancées', 
        } 
        return TemplateResponse(request, 'admin/custom_stats.html', context) 
     
    def index(self, request, extra_context=None): 
        # Statistiques pour le dashboard 
        extra_context = extra_context or {} 
        
        # Récupération des données 
        total_article = Articles.objects.count()
        total_messages = ContactMessage.objects.count() 
        unread_messages = ContactMessage.objects.all() # Ajoutez un champ "lu" si besoin 

         
        extra_context.update({ 
            'total_messages': total_messages, 
            'unread_messages': unread_messages.count(),  
            'total_articles': total_article,  
            'recent_contacts': ContactMessage.objects.all().order_by('-created_at')[:5], 
            'recent_articles': Articles.objects.all().order_by('-created_at')[:5], 
        }) 
         
        return super().index(request, extra_context) 
    
    def login(self, request, extra_context = None):
        extra_context = extra_context or {}
        from django.contrib.auth import login, authenticate

        return super().login(request, extra_context)

    def logout(self, request, extra_context=None):
        """Log out the user and redirect to the admin login page."""
        from django.contrib.auth import logout as auth_logout

        auth_logout(request)
        return redirect('admin:login')


    def Messages_List(self, request):
        messages_qs = ContactMessage.objects.all().order_by('-created_at')
        context = {
            'all_messages': messages_qs,
        }
        return render(request, 'admin/message_list.html', context)
    
    class MessageDeleteView(SuccessMessageMixin, DeleteView):
        model = ContactMessage
        template_name = 'admin/message_confirm_delete.html'
        success_url = reverse_lazy('admin:index')
        success_message = "Félicitation ! Le message supprimé"
    
    
    class ArticleDeleteView(SuccessMessageMixin, DeleteView):
        model = Articles
        template_name = 'admin/article_confirm_delete.html'
        success_url = reverse_lazy('admin:index')
        success_message = "Félicitation ! L'article a été supprimé"

    
    def get_urls(self): 
        urls = super().get_urls() 
        custom_urls = [ 
            path('custom-stats/', self.admin_view(self.custom_stats_view), name='custom_stats'), 
            path('message-delete/?<int:pk>/', self.admin_view(self.MessageDeleteView.as_view()), name='message_delete'), 
            path('aricle-delete/?<int:pk>/', self.admin_view(self.ArticleDeleteView.as_view()), name='aricle_delete'), 
            path('all-messages/', self.admin_view(self.Messages_List), name='messages_list'), 
            path('signup_admin/', self.admin_view(Admin_register), name= 'signup'),
        ] 
        return custom_urls + urls 
     
    
    
    
 
# Remplacez le site admin par défaut 
admin_site = CustomAdminSite(name='custom_admin') 
