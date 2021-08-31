from django.contrib import admin
# from .models import AppUser
from .forms import AppUser, UserForm

# Register your models here.


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'create_time', 'status')
    # fields = ('name', 'phone', 'auth_key', 'email')
    form = UserForm


admin.site.register(AppUser, AppUserAdmin)
