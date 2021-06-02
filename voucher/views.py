from django.shortcuts import render
from django.http import JsonResponse 
from .models import VoucherHDR, VoucherDTL
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .mixins import FieldMixinVoucherDTL
from Accounts.models import KolAcc, MoinAcc, Tafsili,  MoinTafRel 
from extensions.utils import jalalif
from extensions import jalali 
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max
from django.utils.timezone import now
from Company.models import Company

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


class SaveVoucherHdr(LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        import json
        if request.is_ajax:
            VHR = VoucherHDR.objects.filter(Company=request.user.is_company)
            if VHR.exists():
                 
                tmp = VHR.aggregate(Max('VoucherNo'),Max('AtfNo'),Max('FarieNo'))
                VNo = tmp['VoucherNo__max'] +1 
                ANo = tmp['AtfNo__max'] +1 
                FNo = tmp['FarieNo__max'] +1 
            else:
                VNo = 1
                ANo = 1
                FNo = 1

            VDate = json.loads(request.body)["VoucherDate"].strip('\n')
            VDate = jalali.Persian(VDate).gregorian_datetime

            Year = json.loads(request.body)["Year"]
            VKind = json.loads(request.body)["VoucherKind"]
            Cdn = json.loads(request.body)["Condition"]
            VDesc = json.loads(request.body)["VDesc"]

            frm = VoucherHDR(VoucherNo= VNo , AtfNo= ANo, FarieNo= FNo, VoucherDate = VDate, VoucherKind= VKind, Condition= Cdn,
                            Desc= VDesc, Year= Year, UserSabt = request.user ,
                            Company = Company.objects.get(pk=request.user.is_company.pk), DateSabt=now())
            frm.save()
            return JsonResponse({'msg':'success', 'id': frm.id, 'VNo':VNo, 'ANo': ANo})

        else:
            return JsonResponse({'msg':'error'})


class SaveVoucherDtl(LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        import json
        if request.is_ajax:
            print(json.loads(request.body)["Debit"])
            id = json.loads(request.body)["id"]
            Row = json.loads(request.body)["Row"]
            CodeKol = json.loads(request.body)["CodeKol"].strip('\n')
            CodeMoin = json.loads(request.body)["CodeMoin"].strip('\n')
            Taf1 = json.loads(request.body)["Taf1"].strip('\n')
            Taf2 = json.loads(request.body)["Taf2"].strip('\n')
            Taf3 = json.loads(request.body)["Taf3"].strip('\n')
            Taf4 = json.loads(request.body)["Taf4"].strip('\n')
            Disc = json.loads(request.body)["Disc"].strip('\n')
            if json.loads(request.body)["Debit"] != None:
                Debit = json.loads(request.body)["Debit"]
            else:
                Debit = 0
            if json.loads(request.body)["Credit"] != None:
                Credit = json.loads(request.body)["Credit"]
            else:
                Credit = 0
            
            try :
                frm = VoucherDTL()
                frm.VoucherHDR = VoucherHDR.objects.get(pk=id)
                frm.Row = Row
                frm.CodeKol = KolAcc.objects.get(CodeKol__exact=CodeKol, Company=request.user.is_company)
                frm.CodeMoin = CodeMoin = MoinAcc.objects.get(CodeMoin__exact=CodeMoin, Company=request.user.is_company)
                if Taf1 != '' :
                    frm.Taf1 = Tafsili.objects.get(CodeTafsili__exact= Taf1, Company=request.user.is_company)
                if Taf2 != '' :
                    frm.Taf2 = Tafsili.objects.get(CodeTafsili__exact= Taf2, Company=request.user.is_company)
                if Taf3 != '' :
                    frm.Taf3 = Tafsili.objects.get(CodeTafsili__exact= Taf3, Company=request.user.is_company)
                if Taf4 != '' :
                    frm.Taf4 = Tafsili.objects.get(CodeTafsili__exact= Taf4, Company=request.user.is_company)
                frm.Desc = Disc
                frm.Debit = Debit
                frm.Credit = Credit
                frm.UserSabt = request.user
                frm.Company = request.user.is_company 
                frm.save()
            except Exception as e:
                print(e)


            # frm = VoucherDTL(VoucherHDR= VoucherHDR.objects.get(pk=id),Row=Row, 
            #         CodeKol=KolAcc.objects.get(CodeKol__exact=CodeKol, Company=request.user.is_company),
            #         CodeMoin = MoinAcc.objects.get(CodeMoin__exact=CodeMoin, Company=request.user.is_company),
            #         Taf1 = Tafsili.objects.get(CodeTafsili__exact= Taf1, Company=request.user.is_company),
            #         Taf2 = Tafsili.objects.get(CodeTafsili__exact= Taf2, Company=request.user.is_company),
            #         Taf3 = Tafsili.objects.get(CodeTafsili__exact= Taf3, Company=request.user.is_company),
            #         Taf4 = Tafsili.objects.get(CodeTafsili__exact= Taf4, Company=request.user.is_company),
            #         Disc = Disc, Debit=Debit, Credit=Credit)
            
            return JsonResponse({'msg':'success'})
        else:
            return JsonResponse({'msg':'error'})
                    