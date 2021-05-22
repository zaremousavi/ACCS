from django.shortcuts import render
from .models import VoucherHDR
from django.views import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ListVoucher(LoginRequiredMixin,ListView)
