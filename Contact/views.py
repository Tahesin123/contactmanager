from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact

# Create your views here.
def user_index(request):
    
    return render(request,"Contact/index.html",{})

def add_contact(request):
    if request.method=="POST":
       
        
        #fetching the data"
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        Email = request.POST.get("Email")
        work = request.POST.get("work")
        phone = request.POST.get("phone")
        description = request.POST.get("description")

        if len(request.FILES) !=0:
            profileImage = request.FILES['profileImage']
        else:
            profileImage = request.POST.get("contact.png")           


        #Creating model object and set the data
        c = Contact()

        c.firstName = firstName
        c.lastName = lastName
        c.Email = Email
        c.work = work
        c.phone = phone
        c.description = description
        c.profileImage = profileImage

        #Save the Object
        c.save()

        return redirect("/Contact/show-contacts/")
    return render(request,"Contact/add-contact.html",{})

def show_contact(request):
    con = Contact.objects.all()
    return render(request, "Contact/show-contacts.html",{'con': con})   

def delete_contact(request,id):
    print("Contact is ",id)
    cid = Contact.objects.get(pk=id)
    cid.delete()
    return redirect("/Contact/show-contacts/")

def update_contact(request,id):
    cid = Contact.objects.get(pk=id)
    return render(request,"Contact/update_contact.html",{'con':cid})

def updated_contact(request,id):
    if request.method=='POST':
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        Email = request.POST.get("Email")
        work = request.POST.get("work")
        phone = request.POST.get("phone")
        description = request.POST.get("description")
       
        if len(request.FILES) !=0:
            profileImage = request.FILES['profileImage']
        else:
            profileImage = request.POST.get("contact.png")           


        c = Contact.objects.get(pk=id)

        c.firstName = firstName
        c.lastName = lastName
        c.Email = Email
        c.work = work
        c.phone = phone
        c.description = description
        c.profileImage = profileImage

        c.save()
    return redirect("/Contact/show-contacts/")