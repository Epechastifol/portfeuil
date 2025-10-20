
from django.contrib import admin
from Core.admin import admin_site
from .models import ContactMessage

 
class ContactMessageAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read') 
    list_filter = ('created_at', 'is_read') 
    search_fields = ('name', 'email', 'subject', 'message') 
    readonly_fields = ('created_at',) 
    date_hierarchy = 'created_at' 
     
    # Utiliser nos templates personnalisés 
    change_list_template = 'admin/change_list.html' 
    change_form_template = 'admin/change_form.html' 
     
    def get_queryset(self, request): 
        return super().get_queryset(request).select_related() 
     
    def mark_as_read(self, request, queryset): 
        queryset.update(is_read=True) 
    mark_as_read.short_description = "Marquer comme lu"


admin_site.register(ContactMessage, ContactMessageAdmin)
