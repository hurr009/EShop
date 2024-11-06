from django.contrib import admin

from .models import item, category, Order


class Adminitem(admin.ModelAdmin):
    list_display = ['id', 'name', 'original_price', 'category']

class Admincategory(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(item, Adminitem)
admin.site.register(category, Admincategory)
admin.site.register(Order)
