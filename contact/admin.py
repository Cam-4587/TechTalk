from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
    list_filter = ('message', 'read',)
    readonly_fields = ['user', 'name', 'email', 'message']

    fieldsets = (
        ('Contact Message', {
            'fields': ('user', 'name', 'email', 'message')
        }),
        ('Read Status', {
            'fields': ('read',)
        }),
    )


admin.site.register(Contact, ContactAdmin)
