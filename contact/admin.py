from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'phone',
    ordering = 'first_name',
    #list_filter = 'create_date',
    search_fields = 'id', 'first_name',
    list_per_page = 10
    list_max_show_all = 15
    list_editable = 'first_name', 'last_name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'name',


