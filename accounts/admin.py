from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'firs_name', 'last_name', 'username', 'last_login',  'is_active')
    list_display_link = ('email', 'firs_name', 'last_name')
    readonly_fields = ('last_login', 'email')
    ordering = ('email',)

    filter_horizontal=()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)