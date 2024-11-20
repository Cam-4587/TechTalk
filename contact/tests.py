from django.test import TestCase
from .forms import ContactForm


# Create your tests here.
class TestContactForm(TestCase):

    def test_form_is_valid(self):
        
        """ Test for all fields in contact form"""
        
        form = ContactForm({
            'name': 'testuser',
            'email': 'testuser@test.com',
            'message': 'Hello! This is a test message.'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
        
    def test_form_is_valid_without_name(self):
        
        """ test for contact form without name"""
        
        form = ContactForm({
            'name': '',
            'email': 'testuser@test.com',
            'message': 'Hello! This is a test message.'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")
    
    def test_form_is_valid_without_email(self):
        
        """ test for contact form without email"""
        
        form = ContactForm({
            'name': 'testuser',
            'email': '',
            'message': 'Hello! This is a test message.'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_form_is_valid_without_message(self):
        
        """ test for contact form without message"""
        
        form = ContactForm({
            'name': 'testuser',
            'email': 'testuser@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")
        

    