from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email',
                    'telephone',  'category', 'created_at']

    list_display_links = ['id', 'name', 'surname']
    list_per_page = 10
    search_fields = ['name', 'surname', 'telephone', 'email']


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
