from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
    list_filter = ('message', 'read',)
    readonly_fields = ['user','name', 'email','message']
    

class ContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
    list_filter = ('message', 'read',)
    readonly_fields = ['user', 'name', 'email', 'message']

    fieldsets = (
        ('Contact Message',{
            'fields': ('user', 'name', 'email', 'message')  # Readonly fields
        }),
        ('Read Status', {
            'fields': ('read',)  # Editable field
        }),
    )
admin.site.register(Contact, ContactAdmin)
