from django.contrib import admin

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'selling_price', 'discounted_price', 'category']
