from . import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .admin import admin_site
from .views import Profile

urlpatterns = [
    path('', include("Portfolio.urls")),
    path('Blog/', include("Blog.urls")),
    path('admin/', admin_site.urls),
    path('accounts/profile/', Profile, name='profile'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)