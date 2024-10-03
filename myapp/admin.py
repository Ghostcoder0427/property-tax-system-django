# your_app/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import UserRegistration

class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'user_type', 'dob', 'valid_id_link', 'documents_link')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('user_type', 'sex', 'dob')

    # Optional: Add more customization, like date hierarchy or actions
    date_hierarchy = 'dob'
    ordering = ('-dob',)

    def valid_id_link(self, obj):
        if obj.valid_id:
            return format_html('<a href="{}" target="_blank">View ID</a>', obj.valid_id.url)
        return "No ID uploaded"
    valid_id_link.short_description = 'Valid ID'

    def documents_link(self, obj):
        if obj.documents:
            return format_html('<a href="{}" target="_blank">View Documents</a>', obj.documents.url)
        return "No documents uploaded"
    documents_link.short_description = 'Documents'

admin.site.register(UserRegistration, UserRegistrationAdmin)
