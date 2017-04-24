from django.forms import ModelForm
from Inventory.models import Computer


class Inventory_Form(ModelForm):

    class Meta:
        model = Computer

        fields = ['hostname', 'description', 'model', 'serial']

