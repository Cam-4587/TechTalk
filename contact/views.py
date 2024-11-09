from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def ContactFormView(request):
    contactform = ContactForm()
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contact = contactform.save(commit=False)
            contact.user = request.user
            contactform.save()
            return redirect('contact-form')
    
    context = {
        "contactform": contactform
    }
    
    return render(request, 'contact/contact_form.html', context)