from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


def index(request):

    #contacts = Contact.objects.all().order_by('id')
    contacts = Contact.objects.filter(show= True).order_by('id')


    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    


    return render(
        request,
        'contact/index.html',
        context= context
    )

def search(request):
                                           #remove espaços do começo e fim
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects\
                .filter(show= True)\
                .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value) |
                Q(phone__icontains=search_value) |
                Q(email__icontains=search_value)
                )\
                .order_by('id')
    
    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'value_search': search_value
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
    
    contact_name = f'{single_contacts.first_name} {single_contacts.last_name} - '

    context = {
        'contact': single_contacts,
        'site_title': contact_name
    }
    

    return render(
        request,
        'contact/contact.html',
        context= context
    )