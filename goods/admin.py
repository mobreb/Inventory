from django.contrib import admin
from import_export import resources
from .models import Item
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item


class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource


admin.site.register(Item, ItemAdmin)
