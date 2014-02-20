from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from contactapp.forms import Login_details
from contactapp.models import Login
from contactapp.forms import Contact_add1
from contactapp.models import Contacts1




def home(request):  #Displays the Login page
    form=Login_details(request.POST or None)
    return render_to_response('index.html',locals(),context_instance=RequestContext(request))


def contactpage(request):  #Displays Tthe home page
    form=Login_details(request.POST or None)
    if form.is_valid():
        user_id=form.cleaned_data['user_id_number']
        password=form.cleaned_data['password']
        login_credentials=Login.objects.all()[0]
        if login_credentials.user_id_number == user_id and login_credentials.password == password: #username & password check
            return render_to_response('homepage.html',{})
        else:
            return render_to_response('login_error.html',{})


def addcontact(request):    #addingcontacts
    form= Contact_add1(request.POST or None)
    if form.is_valid():
        save_contact = form.save(commit=False)
        save_contact.save()
    return render_to_response('add_contact.html',locals(),context_instance=RequestContext(request))

def displaycontact(request): #displaying contacts
    contactList = []
    contactDetails = []
    for contact in Contacts1.objects.all():
        contactDetails = [contact.contact_first_name,contact.contact_second_name,  contact.contact_number,contact.contact_email_id ]
        print contactDetails
        contactList.append(contactDetails)
        contactList.sort()
    return render_to_response('display_contact.html',{'users':contactList})

def displaycontact_alphabet(request,letter):  #pagenated display
    uppercase_letter=letter.upper()
    contactList = []
    contactDetails = []
    for contact in Contacts1.objects.all():
        if letter==contact.contact_first_name[0] or uppercase_letter==contact.contact_first_name[0]:
         contactDetails = [contact.contact_first_name,contact.contact_second_name,  contact.contact_number,contact.contact_email_id ]
         print contactDetails
         contactList.append(contactDetails)
         contactList.sort()
    return render_to_response('display_contact.html',{'users':contactList})