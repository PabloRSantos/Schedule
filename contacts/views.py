from django.shortcuts import render
from .models import Contact


def index(request):
    contacts = Contact.objects.all

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def contact_profile(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    print(contact)
    return render(request, 'contacts/profile.html', {
        'contact': contact
    })
