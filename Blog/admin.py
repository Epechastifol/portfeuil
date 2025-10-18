from django.contrib import admin
from Core.admin import admin_site
from .models import Articles # Register your models here.


admin_site.register(Articles)
