from django.contrib import admin

# Register your models here.

from .models import Computer


class ComputerAdmin(admin.ModelAdmin):
    search_fields = ('hostname', 'model', 'description', 'serial', 'date')
    list_display = ('hostname', 'model', 'description', 'serial', 'date')


admin.site.register(Computer, ComputerAdmin)