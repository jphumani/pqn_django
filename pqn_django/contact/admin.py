from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'lastname', 'email', 'contact_type', 'created_at', 'subscription')
    search_fields = ('created_at','contact_type', 'email')
    list_filter = ('created_at','contact_type')

admin.site.register(Contact, ContactAdmin)