"""
URL configuration for site_pessoal project.
"""
from django.urls import path, include
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    
    path('login/', views.login_view, name='login'),
    # Ajustado para bater com o nome usado no seu base.html
    path('logout/', views.logout_view, name='logout'),
]

# Servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
