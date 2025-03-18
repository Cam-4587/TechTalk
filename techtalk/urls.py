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
    path(
        'ckeditor/upload/',
        login_required(views.upload),
        name='ckeditor_upload'
    ),
    path(
        'ckeditor/browse/',
        login_required(views.browse),
        name='ckeditor_browse'
    ),
]
