from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
    list_filter = ('message', 'read',)

admin.site.register(Contact, ContactAdmin)
