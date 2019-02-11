from django.contrib import admin
from .models import  Number

class NumberAdmin(admin.ModelAdmin):
    fields = ['description_text', 'value']
    
admin.site.register(Number)