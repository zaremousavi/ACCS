from django.shortcuts import render
from django.http import JsonResponse 
from .models import VoucherHDR, VoucherDTL
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .mixins import FieldMixinVoucherDTL
from Accounts.models import KolAcc, MoinAcc, Tafsili,  MoinTafRel 
from extensions.utils import jalalif
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

class ListVoucher(LoginRequiredMixin,ListView):
    template_name = 'voucher/voucherList.html'
    model = VoucherHDR
    def get_queryset(self):
        return VoucherHDR.objects.filter(Company=self.request.user.is_company)

@login_required
def PreCreateVoucher(request):
    import json
    moin = MoinAcc.objects.filter(Company=request.user.is_company).values_list('CodeKol__CodeKol','CodeKol__TitleKol','CodeMoin','TitleMoin')
    mtr = MoinTafRel.objects.filter(Company= request.user.is_company).values_list('Moin__CodeMoin','Level','GroupTaf__CodeGroupTaf')
    tf = Tafsili.objects.filter(Company=request.user.is_company).values_list('CodeGroupTaf__CodeGroupTaf','CodeTafsili', 'TitleTafsili')
    moins = json.dumps(list(moin), cls=DjangoJSONEncoder)
    mtrs =  json.dumps(list(mtr), cls= DjangoJSONEncoder)
    tfs = json.dumps(list(tf), cls=DjangoJSONEncoder)
    time = jalalif(timezone.now())
    return render(request,'voucher/voucherCreate.html',{'kolmoins':moins,'mtrs':mtrs, 'tf': tfs ,'tms':time})

#kolCheck
class KolCheck(LoginRequiredMixin,CreateView):
    def post(self, request, *args, **kwargs):
        import json
        if request.is_ajax():
            Kl = json.loads(request.body)["kol"].strip('\n')
            q = KolAcc.objects.filter(CodeKol__exact=Kl, Company=request.user.is_company)
            if not q.exists() :
                return JsonResponse({'msg':'error'})
            else:
                title = q.values_list('TitleKol')
                return JsonResponse({'msg':'success','title': list(title)})

        else:
            return JsonResponse({'msg':'error in loading ajax...'})


#Moin Check by Ajax
class MoinCheck(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        import json
        if request.is_ajax():
            Kl = json.loads(request.body)["kol"].strip('\n')
            moin = json.loads(request.body)["moin"].strip('\n')

            q= MoinAcc.objects.filter(CodeKol__CodeKol__exact=Kl,CodeMoin__exact=moin ,Company=request.user.is_company)
            
            if not q.exists() :
                return JsonResponse({'msg':'error'})
            else:
                title= q.values_list('TitleMoin')
                return JsonResponse({'msg':'success', 'title': list(title)})

        else:
            return JsonResponse({'msg':'error in loading ajax...'})
