from django.db import models
from authent.models import User
from Company.models import Company
from django.utils.timezone import now
from django.urls import reverse
from extensions.utils import jalali_converter
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class GroupAcc(models.Model):
    getchoice = {("1", "ترازنامه ای"), ("2", "سود و زیانی"), ("3", "کنترلی")}
    CodeGroup = models.CharField(max_length=2, verbose_name='کد گروه')
    TitleGroup = models.CharField(max_length=150, verbose_name='عنوان گروه')
    kind = models.CharField(max_length=1, choices=getchoice, verbose_name='نوع')
    UserSabt = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='کاربر ثبت کننده')
    DateSabt = models.DateTimeField(default=now, auto_created=True, verbose_name='تاریخ ایجاد')
    # Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='شرکت')

    def __str__(self):
        return '%s--%s' % (self.CodeGroup, self.TitleGroup)

    def get_absolute_url(self):
        return reverse("Accounts:CreateGroupAcc")

    def JDateSabt(self):
        return jalali_converter(self.DateSabt)

    def Kind_s(self):
        if self.kind == "1":
            mystr = "ترازنامه ای"
        elif self.kind == "2":
            mystr = "سود و زیانی"
        elif self.kind == "3":
            mystr = "کنترلی"
        return mystr

    Kind_s.short_description = 'نوع حساب'

    class Meta:
        verbose_name= 'گروه حسابها'
        db_table = 'GroupAcc'
        ordering = ['CodeGroup']
        # unique_together = ['CodeGroup', 'Company']
        indexes = [
            models.Index(fields=['id']),
        ]


class KolAcc(models.Model):
    getchoice1 = (("1", "بدهکار مطلق"), ("2", "بدهکار"), ("3", "بستانکار مطلق"), ("4", "بستانکار"), ("5", "بدون کنترل"))
    CodeGroup = models.ForeignKey(GroupAcc, on_delete=models.CASCADE, verbose_name=' گروه حساب')
    CodeKol = models.CharField(max_length=5, verbose_name='کد کل')
    TitleKol = models.CharField(max_length=150, verbose_name='عنوان حساب کل')
    kind = models.CharField(max_length=1, choices=getchoice1, verbose_name='نوع حساب')
    UserSabt = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='کاربر ثبت کننده')
    DateSabt = models.DateTimeField(default=now, auto_created=True, verbose_name='تاریخ ایجاد')
    # Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='شرکت')

    def __str__(self):
        return '%s %s' % (self.CodeKol, self.TitleKol)

    def JDateSabt(self):
        return jalali_converter(self.DateSabt)

    def Kind_s(self):
        if self.kind == "1":
            mystr = "بدهکار مطلق"
        elif self.kind == "2":
            mystr = "بدهکار"
        elif self.kind == "3":
            mystr = "بستانکار مطلق"
        elif self.kind == "4":
            mystr = "بستانکار"
        elif self.kind == "5":
            mystr = "بدون کنترل"
        return mystr

    Kind_s.short_description = 'نوع حساب'

    def get_absolute_url(self):
        return reverse("Accounts:CreateKolAcc")

    class Meta:
        verbose_name= 'حساب کل'
        db_table = 'KolAcc'
        ordering = ['CodeKol']
        # unique_together = ['CodeKol', 'Company']
        indexes = [
            models.Index(fields=['id']),
        ]


class MoinAcc(models.Model):
    CodeKol = models.ForeignKey(KolAcc, on_delete=models.CASCADE, verbose_name='حساب کل')
    CodeMoin = models.CharField(max_length=10, verbose_name='کد معین')
    TitleMoin = models.CharField(max_length=150, verbose_name='عنوان حساب معین')
    Kind = models.IntegerField(verbose_name='نوع')
    TafRel = models.IntegerField(default=0, verbose_name='ارتباط با تفصیلی')
    # Arz =
    UserSabt = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='کاربر ثبت کننده')
    DateSabt = models.DateTimeField(default=now, auto_created=True, verbose_name='تاریخ ایجاد')
    # Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='شرکت')

    def __str__(self):
        return '%s %s' % (self.CodeMoin, self.TitleMoin)

    def JDateSabt(self):
        return jalali_converter(self.DateSabt)

    def get_absolute_url(self):
        return reverse("Accounts:ListMoinAcc")

    class Meta:
        verbose_name= 'حساب معین'
        db_table = 'MoinAcc'
        ordering = ['CodeMoin']
        # unique_together = ['CodeMoin', 'Company']
        indexes = [
            models.Index(fields=['id']),
        ]

class GroupTaf(models.Model):
    CodeGroupTaf = models.CharField(max_length=5, verbose_name='کد گروه تفصیلی')
    TitleGroupTaf = models.CharField(max_length=150, verbose_name='عنوان گروه تفصیلی')
    UserSabt = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='کاربر ثبت کننده')
    DateSabt = models.DateTimeField(default=now, auto_created=True, verbose_name='تاریخ ایجاد')
    # Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='شرکت')

    def __str__(self):
        return '%s %s' % (self.CodeGroupTaf, self.TitleGroupTaf)

    def JDateSabt(self):
        return jalali_converter(self.DateSabt)

    def get_absolute_url(self):
        return reverse("Accounts:ListGroupTaf")

    class Meta:
        verbose_name= 'گروه تفصیلی'
        db_table = 'GroupTaf'
        ordering = ['CodeGroupTaf']
        # unique_together = ['CodeGroupTaf', 'Company']
        indexes = [
            models.Index(fields=['id']),
        ]
# تفصیلی
class Tafsili(models.Model):
    ActiveChoice = (("0", "غیر فعال"), ("1", "فعال"))
    TaxChoice = (("1", "مالیاتی"), ("2", "غیر مالیاتی"))

    CodeTafsili = models.CharField(max_length=10, verbose_name='کد تفصیلی')
    TitleTafsili = models.CharField(max_length=150, verbose_name='عنوان تفصیلی')
    CodeGroupTaf = models.ForeignKey(GroupTaf, on_delete=models.CASCADE, verbose_name='گروه تفصیلی')
    Tozihat = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    is_Active = models.CharField(max_length=1, default="1", choices=ActiveChoice, verbose_name='وضعیت فعال')
    is_Tax = models.CharField(max_length=1, choices=TaxChoice, verbose_name='وضعیت مالیاتی')
    UserSabt = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='کاربر ثبت کننده')
    DateSabt = models.DateTimeField(default=now, auto_created=True, verbose_name='تاریخ ایجاد')
    # Company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='شرکت')

    def __str__(self):
        return '%s %s' % (self.CodeTafsili, self.TitleTafsili)

    def JDateSabt(self):
        return jalali_converter(self.DateSabt)

    def get_absolute_url(self):
        return reverse("Accounts:ListTafsili")

    def Tax(self):
        if self.is_Tax=='1':
            return 'مالیاتی'
        else:
            return 'غیر مالیاتی'

    def Con(self):
        if self.is_Tax=='0':
            return 'غیر فعال'
        else:
            return 'فعال'

    class Meta:
        verbose_name= 'تفصیلی'
        db_table = 'Tafsili'
        ordering = ['CodeTafsili']
        # unique_together = ['CodeTafsili', 'Company']
        indexes = [
            models.Index(fields=['id']),
        ]

class MoinTafRel(models.Model):
    Moin = models.ForeignKey(MoinAcc,on_delete=models.CASCADE, verbose_name='حساب معین')
    Level = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)],verbose_name='سطح تفصیلی')
    GroupTaf = models.ForeignKey(GroupTaf,blank=True, null=True, on_delete= 'گروه تفصیلی')

    class Meta:
        verbose_name= 'ارتباط معین با گروه تفصیلی'
        db_table = 'MoinTafRel'
