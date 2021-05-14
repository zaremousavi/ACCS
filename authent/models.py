from django.db import models
from django.contrib.auth.models import AbstractUser
from Company.models import Company
# Create your models here.

class User(AbstractUser):
    is_company = models.ForeignKey(Company,null=True, blank=True,on_delete=models.CASCADE, verbose_name='نام شرکت')
    is_admin_company = models.BooleanField(default=False, verbose_name='ادمین شرکت')
    mobile = models.CharField(max_length=10, blank=True, null=True, verbose_name='تلفن همراه')
    def is_company_active(self):
        if (Company.is_active):
            return True
        else:
            return False

    is_company_active.boolean = True
    is_company_active.short_description= 'وضعیت شرکت کاربر'