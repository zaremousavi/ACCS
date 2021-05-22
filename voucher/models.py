from django.db import models
from django.utils.timezone import now
from authent.models import User
from Company.models import Company
from extensions.utils import jalali_converter
from Accounts.models import KolAcc, MoinAcc, Tafsili, MoinTafRel
from django.core.exceptions import ValidationError
# Create your models here.


class VoucherHDR(models.Model):
    Kindchoice = {("1", "عمومی"), ("2", "درآمد"), ("3", "حقوق و دسمتزد")}
    ConditionChoice = {(1,'یادداشت'),(2 ,'ثبت'), (3,'تایید شده'), (4,'قطعی')}
    VoucherNo = models.IntegerField(verbose_name='شماره سند')
    AtfNo = models.IntegerField(verbose_name='شماره عطف')
    FarieNo = models.IntegerField(verbose_name='شماره فرعی')
    VoucherDate = models.DateTimeField(auto_now=True,verbose_name='شماره عطف')
    VoucherKind = models.CharField(max_length=1, default="1",choices= Kindchoice, verbose_name='نوع سند' ) 
    Condition = models.IntegerField(default=0, choices=ConditionChoice, verbose_name='وضعیت سند')
    Desc = models.TextField(blank=True, null= True, verbose_name='شرح سند')
    Year = models.CharField(max_length=4,verbose_name='سال مالی')


    UserSabt = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='Sabt', verbose_name='کاربر ثبت کننده')
    UserCheck = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='Check', verbose_name='کاربر تایید کننده')
    DateSabt = models.DateTimeField(default=now, auto_created=True, verbose_name='تاریخ ایجاد')
    Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='شرکت')

    def __str__(self):
        return '{}--{}--{}'.format(self.VoucherNo, self.JDate, self.Condition)

    def JDate(self):
        return jalali_converter(self.VoucherDate)

    def Kinds(self):
        K = ['عمومی','درآمد','حقوق و دستمزد']
        return K[int(self.VoucherKind)-1]
    def Conds(self):
        C = ['یادداشت','ثبت','تایید ','قطعی']    
        return C[self.Condition-1]
    
    class Meta:
        verbose_name= 'سند'
        db_table = 'VoucherHDR'
        ordering = ['VoucherNo']
        unique_together = ['VoucherNo', 'Company']
        indexes = [
            models.Index(fields=['id']),
        ]

# جزییات سند 


class VoucherDTL(models.Model):


    VoucherHDR= models.ForeignKey(VoucherHDR,  on_delete=models.DO_NOTHING, verbose_name= "شماره سند")
    CodeKol = models.ForeignKey(KolAcc, on_delete=models.DO_NOTHING, verbose_name=("حساب کل"))
    CodeMoin = models.ForeignKey(MoinAcc, on_delete=models.DO_NOTHING, verbose_name=("حساب معین"))
    Taf1 = models.ForeignKey(Tafsili, on_delete=models.DO_NOTHING,related_name='Taf1', verbose_name=("حساب تفصیلی ۱"))
    Taf2 = models.ForeignKey(Tafsili, on_delete=models.DO_NOTHING,related_name='Taf2', verbose_name=("حساب تفصیلی ۲"))
    Taf3 = models.ForeignKey(Tafsili, on_delete=models.DO_NOTHING,related_name='Taf3', verbose_name=("حساب تفصیلی ۳"))
    Taf4 = models.ForeignKey(Tafsili, on_delete=models.DO_NOTHING,related_name='Taf4', verbose_name=("حساب تفصیلی ۴"))
    Disc = models.CharField(max_length=200,null=True, blank=True, verbose_name='شرح ردیف سند')
    Debit = models.DecimalField(max_digits=20,decimal_places=0,verbose_name='بدهکار')
    Credit = models.DecimalField(max_digits=20,decimal_places=0,verbose_name='بستانکار')
    File = models.FileField(verbose_name='فایل پیوست')
    UserSabt = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='کاربر')
    Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='شرکت')


    class Meta:
        verbose_name= 'جزییات سند'
        db_table = 'VoucherDTL'
        indexes = [
            models.Index(fields=['id']),
        ]

