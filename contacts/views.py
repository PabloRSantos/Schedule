from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.core.paginator import Paginator


def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        show=True
    )
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def contact_profile(request, contact_id):
    # contact = Contact.objects.get(id=contact_id)
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.show:
        raise Http404()

    return render(request, 'contacts/profile.html', {
        'contact': contact
    })
