from . import views
from django.urls import path

urlpatterns = [
    path('contact-form/', views.ContactFormView, name="contact-form")
]
