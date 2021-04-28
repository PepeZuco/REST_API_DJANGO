from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from system.models import Client, Purchase

class Clients(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_per_page = 20

admin.site.register(Client, Clients)

class Purchases(admin.ModelAdmin):
    list_display = ('client','price')
    list_display_links = ('client','price')   

admin.site.register(Purchase, Purchases)
