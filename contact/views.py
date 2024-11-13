from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.

def ContactFormView(request):
    contactform = ContactForm()
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contact = contactform.save(commit=False)
            if request.user.is_authenticated:
                contact.user = request.user
            else:
                contact.user = None
            contactform.save()
            return redirect('contact-form')
    
    context = {
        "contactform": contactform
    }
    
    return render(request, 'contact/contact_form.html', context)