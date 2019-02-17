from django.contrib import admin
from .models import  Number

class NumberAdmin(admin.ModelAdmin):
    fields = ['__all__']
    #list_display = ('description_text', 'value','unit','link','pub_date')
    list_filter = ['unit']

    
admin.site.register(Number)