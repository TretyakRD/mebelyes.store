from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'tel', 'total_price', 'date']
    list_display_links = list_display
    list_filter = ['date']