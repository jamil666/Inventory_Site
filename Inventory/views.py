from django.http import HttpResponse
from django.shortcuts import render, redirect
from Inventory.models import Computer
from .forms import Inventory_Form
from django.db.models import Q
import datetime

# Create your views here.

def main(request):
    CompDB = Computer.objects.all()
    Form = Inventory_Form(request.POST)

    if request.method == "POST":
        SearchField = request.POST.get('search')
        try:
            Search = Computer.objects.filter(Q(hostname__contains=SearchField) |
                                             Q(description__contains=SearchField) |
                                             Q(model__contains=SearchField) |
                                             Q(serial__contains=SearchField))

            context = {"Form": Form, "CompDB": CompDB, "Search":  Search}
            return render(request, 'main.html', context)
        except:
            context = {"Form": Form, "CompDB": CompDB, "Message": "Record not found!"}
            return render(request, 'main.html', context)

    context = {"Form": Form, "CompDB": CompDB}
    return render(request, 'main.html', context)

def AddNew(request):
    CompDB = Computer.objects.all()
    date = datetime.datetime.now()

    Form = Inventory_Form(request.POST)
    context = {"Form": Form, "CompDB": CompDB}

    if request.method == 'POST':
        Hostname = request.POST.get('hostname')
        Description = request.POST.get('description')
        Model = request.POST.get('model')
        Serial = request.POST.get('serial')

        Database = Computer(hostname=Hostname, description=Description, model=Model, serial=Serial, date=date.strftime("%d %b %Y"))
        Database.save()

        return redirect(main)

    return render(request, 'AddNew.html', context)


def Edit(request):
    CompDB = Computer.objects.all()
    Form = Inventory_Form(request.POST)
    date = datetime.datetime.now()

    id = request.GET.get("id")
    edited_device = Computer.objects.get(id=id)

    if request.method == "POST":

        hostname = request.POST.get("hostname")
        description = request.POST.get("description")
        model = request.POST.get("model")
        serial = request.POST.get("serial")

        CompDB.filter(id=id).update(hostname=hostname, description=description, model=model, serial=serial, date=date.strftime("%d %b %Y"))

        return redirect(main)

    context = {"Form": Form, "CompDB": CompDB, "Edited_device": edited_device}
    return render(request, 'Edit.html', context)


def Delete(request):
    id = request.GET.get("id")
    deleted_item = Computer.objects.get(id=id)
    deleted_item.delete()
    return redirect(main)
