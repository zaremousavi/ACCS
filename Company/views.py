from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

# class Test(LoginRequiredMixin,ListView):
#     queryset= Model.objects.all()
#     template_name = ''