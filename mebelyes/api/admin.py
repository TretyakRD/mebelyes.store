from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'slug', 'prices']
    list_display_links = list_display
    list_filter = ['category']

@admin.register(Service)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'description']
    list_display_links = list_display
    list_filter = ['slug']

@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = list_display
    list_filter = ['id']