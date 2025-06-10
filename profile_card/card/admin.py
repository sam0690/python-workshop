from django.contrib import admin
from .models import Profile  
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'location', 'birth_date')  # Adjust fields as per your Profile model
    search_fields = ('name', 'bio', 'location')  # Assuming user is a ForeignKey to User model
    list_filter = ('location',)  # Add filters as needed

admin.site.register([Profile])  # Register your models here, if any