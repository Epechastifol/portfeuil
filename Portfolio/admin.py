
from django.contrib import admin
from Core.admin import admin_site
from .models import ContactMessage

 


admin_site.register(ContactMessage)
