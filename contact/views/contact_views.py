from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

# Create your views here.


def index(request):

    #contacts = Contact.objects.all().order_by('id')
    contacts = Contact.objects.filter(show= True).order_by('id')[0:10]
    context = {
        'contacts': contacts
    }
    

    return render(
        request,
        'contact/index.html',
        context= context
    )



def contact(request, contact_id):

    #pode gerar problema no get se nao encontrar o valor
    #single_contacts = Contact.objects.get(pk= contact_id)

    """ single_contacts = Contact.objects.filter(pk= contact_id).first()

    if single_contacts is None:
        raise Http404()  """
    
    #usando o get_or_404
    single_contacts = get_object_or_404(
        Contact,
        pk=contact_id,
        show = True
        )

    context = {
        'contact': single_contacts
    }
    

    return render(
        request,
        'contact/contact.html',
        context= context
    )