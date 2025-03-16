"""
URL configuration for techtalk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls"), name='blog'),
    path('about/', include("about.urls"), name='about'),
    path('contact/', include("contact.urls"), name='contact'),
    path("accounts/", include("allauth.urls")),
    path('ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', login_required(views.browse), name='ckeditor_browse'),
]
