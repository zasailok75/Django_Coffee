from django.contrib import admin  
from .models import Coffee  # Make sure to import your model  

class CoffeeAdmin(admin.ModelAdmin):  
    list_display = ('name', 'price', 'quantity')  # Use '=' instead of calling it as a function  

admin.site.register(Coffee, CoffeeAdmin)