from django.contrib import admin
from profiles.models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'country',
        'city',
        'zip_code',
        'address_first',
        'address_second',
        'info',
    ]

admin.site.register(Profile, ProfileAdmin)
