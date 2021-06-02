from django.urls import path
from . import views


app_name = 'Voucher'

urlpatterns = [
    path('ListVoucher',views.ListVoucher.as_view(),name='ListVoucher'),
    path('PreCreateVoucher',views.PreCreateVoucher,name='PreCreateVoucher'),
    path('SaveVoucherHdr', views.SaveVoucherHdr.as_view(), name='SaveVoucherHdr'),
    path('SaveVoucherDtl', views.SaveVoucherDtl.as_view(), name='SaveVoucherDtl'),

]