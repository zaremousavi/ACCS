from django.db import models
from django.utils import timezone
# Create your models here.
class Company(models.Model):
    Code = models.IntegerField(unique=True, verbose_name='کد شرکت')
    Title = models.CharField(max_length=200, verbose_name='نام شرکت')
    DateCreate = models.DateTimeField(auto_created=True, verbose_name='تاریخ ایجاد')
    Conditions = models.IntegerField(default=1, verbose_name='وضعیت')
    CreditDate = models.DateTimeField(verbose_name='اعتبار تاریخ')


    def is_active(self):
        if (self.CreditDate > timezone.now()):
            return True
        else:
            return False


    def __str__(self):
        return self.Title

    class Meta:
        verbose_name= 'شرکت'
        db_table = 'Company'
        ordering = ['Code']
        indexes = [
            models.Index(fields=['Code']),
        ]