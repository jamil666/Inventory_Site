from django.shortcuts import render, redirect
from Inventory.models import Computer
from .forms import Inventory_Form
from django.db.models import Q
import datetime


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# Main page

@login_required                                     # Main page can be only by authenticated user
def main(request):
    CompDB = Computer.objects.all()                 # Get all objects from Database

    if request.method == "POST":
        SearchField = request.POST.get('search')    # Get query from Search Field

        Search = Computer.objects.filter(Q(hostname__contains=SearchField) |            # Find object by query
                                             Q(description__contains=SearchField) |
                                             Q(model__contains=SearchField) |
                                             Q(serial__contains=SearchField) |
                                             Q(date__contains=SearchField))

        context = {"CompDB": CompDB, "Search": Search}
        return render(request, 'main.html', context)

    context = {"CompDB": CompDB}
    return render(request, 'main.html', context)

# Add new item to database

def AddNew(request):
    CompDB = Computer.objects.all()                     # Get all objects from Database
    date = datetime.datetime.now()                      # Get current time

    Form = Inventory_Form(request.POST)
    context = {"Form": Form, "CompDB": CompDB}

    if request.method == 'POST':
        try:
            Hostname = request.POST.get('hostname')
            Description = request.POST.get('description')
            Model = request.POST.get('model')
            Serial = request.POST.get('serial')

            # Save new object to database

            Database = Computer(hostname=Hostname, description=Description, model=Model, serial=Serial, date=date.strftime("%d %b %Y"))
            Database.save()
            return redirect(main)                       # Redirect to main page after successful adding new computer

        except:
            context = {"Form": Form, "CompDB": CompDB,
                       "Message": "Computer with Hostname '%s' or Serial '%s' already exist in database!" %(Hostname, Serial)}
            return render(request, 'AddNew.html', context)


    return render(request, 'AddNew.html', context)

# Edit records view

def Edit(request):
    CompDB = Computer.objects.all()                 # Get all objects from Database

    date = datetime.datetime.now()

    id = request.GET.get("id")                      # Get object ID from request
    edited_device = Computer.objects.get(id=id)     # Find computer object from database by ID

    if request.method == "POST":

        # Add new values to computer object. If no new values, old value should be used

        hostname = request.POST.get("hostname")
        description = request.POST.get("description")
        model = request.POST.get("model")
        serial = request.POST.get("serial")

        CompDB.filter(id=id).update(hostname=hostname, description=description, model=model, serial=serial, date=date.strftime("%d %b %Y"))

        return redirect(main)

    context = {"CompDB": CompDB, "Edited_device": edited_device}
    return render(request, 'Edit.html', context)

# Delete item from database

def Delete(request):
    id = request.GET.get("id")                      # Get object ID from request
    deleted_item = Computer.objects.get(id=id)      # Find computer object from database by ID
    deleted_item.delete()                           # Delete selected object from database
    return redirect(main)


# Login page

def Login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)       # Authenticate user
            login(request, user)

            return redirect(main)                                     # Redirect to main page if authentication success

        except:

            # Insert error message to login page

            context = {"ErrorMessage": "Your username or password didn't match. Please try again."}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

