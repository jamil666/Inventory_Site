from django.shortcuts import render, redirect
from Inventory.models import Computer
from .forms import Inventory_Form
from django.db.models import Q

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
            context = {"Form": Form, "CompDB": CompDB, "Message": "Record not founf!"}
            return render(request, 'main.html', context)

    context = {"Form": Form, "CompDB": CompDB}
    return render(request, 'main.html', context)

def AddNew(request):
    CompDB = Computer.objects.all()

    Form = Inventory_Form(request.POST)
    context = {"Form": Form, "CompDB": CompDB}

    if request.method == 'POST':
        Hostname = request.POST.get('hostname')
        Description = request.POST.get('description')
        Model = request.POST.get('model')
        Serial = request.POST.get('serial')

        print(Hostname, Description, Model, Serial)

        Database = Computer(hostname=Hostname, description=Description, model=Model, serial=Serial)
        Database.save()

        return redirect(main)

    return render(request, 'AddNew.html', context)
