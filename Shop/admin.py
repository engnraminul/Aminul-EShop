from django.contrib import admin
from Shop.models import Category, Product

# Register your models here.

def duplicate_event(modeladmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
duplicate_event.short_description = "Clone"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_name', 'Category', 'created_date', 'price')
    list_filter = ('Category',)
    search_fields = ('Product_name',)
    actions = [duplicate_event]

    





admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
