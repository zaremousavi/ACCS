from django.urls import path
from . import views


app_name = 'Voucher'

urlpatterns = [
    path('ListVoucher',views.ListVoucher.as_view(),name='ListVoucher'),
    path('PreCreateVoucher',views.PreCreateVoucher,name='PreCreateVoucher'),
    path('KolCheck', views.KolCheck.as_view(), name='KolCheck'),
    path('MoinCheck', views.MoinCheck.as_view(), name='MoinCheck'),

]