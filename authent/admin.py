from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
UserAdmin.fieldsets += (
    ("فیلد های جدید", {'fields': ('is_company','is_admin_company')}),
)
UserAdmin.list_display += ('is_company','is_admin_company','is_company_active')
admin.site.register(User, UserAdmin)