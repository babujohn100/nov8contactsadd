from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactsForm


# Create your views here.

def view_contacts(request):
    contacts=Contact.objects.all()
    return render(request, "contacts/index.html",{"contacts":contacts})
    
def add_contacts(request):
    if request.method=="POST":
        form = ContactsForm(request.POST)
        form.save()
        return redirect("/")
        
    contacts=ContactsForm()
    return render(request, "contacts/add_contacts.html",{"form":contacts})

def edit_contact(request, id):
    contact=Contact.objects.get(id=id)
    if request.method == "POST":
        form = ContactsForm(request.POST, instance=contact)
        form.save()
        return redirect("/")
    
    form = ContactsForm(instance=contact)
    return render(request, "contacts/add_contacts.html", {"form":form, "title": "Edit"})


