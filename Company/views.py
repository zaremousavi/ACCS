from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from extensions.utils import jalali_converter, jalalis
from django.utils.timezone import now
# Create your views here.
@login_required
def home(request):
    jalali = jalalis(now())
    return render(request,'home.html',{'Jtime':jalali})

# class Test(LoginRequiredMixin,ListView):
#     queryset= Model.objects.all()
#     template_name = ''