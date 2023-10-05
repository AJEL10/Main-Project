from django.contrib import admin
from .models import Usertable

# Register your Usertable model with the admin site
@admin.register(Usertable)
class UsertableAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth')  # Define the fields to display in the list view
    search_fields = ('username', 'email')  # Add fields you want to search by
    list_filter = ('date_of_birth',)  # Add filters for the list view
