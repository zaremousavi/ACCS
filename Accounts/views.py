from django.db.models.aggregates import Count
from django.shortcuts import render
from .models import GroupAcc, KolAcc, MoinAcc, GroupTaf, Tafsili, MoinTafRel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormValidMixin, FieldMixin, FieldKolMixin, FormValidKolMixin, FieldMoinMixin, FormValidMoinMixin, \
    AccessMixin
from .mixins import AccessKolMixin, AccessMoinMixin, AccessGroupTafMixin, FieldGroupTafMixin, FormValidGroupTafMixin
from .mixins import FormValidTafsiliMixin, AccessTafsiliMixin, FieldTafsiliMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import MoinTafRelForm
from django.utils.timezone import now
from authent.models import User
from Company.models import Company
# Create your views here.

class ListGroupAcc(LoginRequiredMixin, ListView):
    template_name = 'Account/GroupAcc.html'

    def get_queryset(self):
        return GroupAcc.objects.filter(Company=self.request.user.is_company)


class CreateGroupAcc(LoginRequiredMixin, FormValidMixin, FieldMixin, CreateView):
    model = GroupAcc
    template_name = 'Account/GroupAccCreateUpdate.html'


class UpdateGroupAcc(AccessMixin, FormValidMixin, FieldMixin, UpdateView):
    model = GroupAcc
    template_name = 'Account/GroupAccCreateUpdate.html'


class DeleteGroupAcc(AccessMixin, DeleteView):
    model = GroupAcc
    template_name = 'Account/GroupAccCreateUpdate.html'


# kol
class ListKolAcc(LoginRequiredMixin, ListView):
    template_name = 'Account/KolAcc.html'

    def get_queryset(self):
        return KolAcc.objects.filter(Company=self.request.user.is_company)


class CreateKolAcc(LoginRequiredMixin, FormValidKolMixin, FieldKolMixin, CreateView):
    model = KolAcc
    template_name = 'Account/KolAccCreateUpdate.html'


class UpdateKolAcc(AccessKolMixin, FormValidKolMixin, FieldKolMixin, UpdateView):
    model = KolAcc
    template_name = 'Account/KolAccCreateUpdate.html'


class DeleteKolAcc(AccessKolMixin, FormValidKolMixin, FieldKolMixin, DeleteView):
    model = KolAcc
    template_name = 'Account/KolAccCreateUpdate.html'


# moin

class ListMoinAcc(LoginRequiredMixin, ListView):
    template_name = 'Account/MoinAcc.html'

    def get_queryset(self):
        return MoinAcc.objects.filter(Company=self.request.user.is_company)


class CreateMoinAcc(LoginRequiredMixin, FormValidMoinMixin, FieldMoinMixin, CreateView):
    model = MoinAcc
    template_name = 'Account/MoinAccCreateUpdate.html'


class UpdateMoinAcc(AccessMoinMixin, FormValidMoinMixin, FieldMoinMixin, UpdateView):
    model = MoinAcc
    template_name = 'Account/MoinAccCreateUpdate.html'


class DeleteMoinAcc(AccessMoinMixin, FormValidMoinMixin, FieldMoinMixin, DeleteView):
    model = MoinAcc
    template_name = 'Account/MoinAccCreateUpdate.html'

# GroupTaf

class ListGroupTaf(LoginRequiredMixin, ListView):
    template_name = 'Account/GroupTaf.html'

    def get_queryset(self):
        return GroupTaf.objects.filter(Company=self.request.user.is_company)


class CreateGroupTaf(LoginRequiredMixin, FormValidGroupTafMixin, FieldGroupTafMixin, CreateView):
    model = GroupTaf
    template_name = 'Account/GroupTafCreateUpdate.html'


class UpdateGroupTaf(AccessGroupTafMixin, FormValidGroupTafMixin, FieldGroupTafMixin, UpdateView):
    model = GroupTaf
    template_name = 'Account/GroupTafCreateUpdate.html'


class DeleteGroupTaf(AccessGroupTafMixin, FormValidGroupTafMixin, FieldGroupTafMixin, DeleteView):
    model = GroupTaf
    template_name = 'Account/GroupTafCreateUpdate.html'

#tafsili

class ListTafsili(LoginRequiredMixin, ListView):
    template_name = 'Account/Tafsili.html'

    def get_queryset(self):
        return Tafsili.objects.filter(Company=self.request.user.is_company)


class CreateTafsili(LoginRequiredMixin, FormValidTafsiliMixin, FieldTafsiliMixin, CreateView):
    model = Tafsili
    template_name = 'Account/TafsiliCreateUpdate.html'


class UpdateTafsili(AccessGroupTafMixin, FormValidTafsiliMixin, FieldTafsiliMixin, UpdateView):
    model = Tafsili
    template_name = 'Account/TafsiliCreateUpdate.html'


class DeleteTafsili(AccessTafsiliMixin, FormValidTafsiliMixin, FieldTafsiliMixin, DeleteView):
    model = GroupTaf
    template_name = 'Account/TafsiliCreateUpdate.html'


def ListMoinTafRel(request):
    Moin = MoinAcc.objects.filter(Company=request.user.is_company)
    GTafs = GroupTaf.objects.filter(Company=request.user.is_company)
    return render(request, 'Account/MoinTafRel.html', {'Moins':Moin, 'GTaf':GTafs})

@login_required
def CheckGtaf(request):
    import json
    if (request.is_ajax() and request.method=='POST'):
        Gta = json.loads(request.body)["Gtaf"].strip('\n')#request.POST.get('Gtaf')
        print(Gta)
        q = GroupTaf.objects.filter(CodeGroupTaf__exact= Gta, Company=request.user.is_company).count()
        if q==0 :
            return JsonResponse({'msg':'error'})
        else:
            return JsonResponse({'msg':'success'})
    else:
        return JsonResponse({'msg':'NO ajax'})

class CheckGtafs(LoginRequiredMixin,CreateView):
    def post(self, request, *args, **kwargs):
        import json
        if request.is_ajax():
            Gta = json.loads(request.body)["Gtaf"].strip('\n')
            q= GroupTaf.objects.filter(CodeGroupTaf__exact=Gta, Company=request.user.is_company).exists()
            
            if not q :
                return JsonResponse({'msg':'error'})
            else:
                moin = json.loads(request.body)["moin"].strip('\n')
                level = json.loads(request.body)["level"]
                print(now)
                frm= MoinTafRel(Moin=MoinAcc.objects.get(CodeMoin__exact=moin,  Company=request.user.is_company),
                    Level=int(level),GroupTaf = GroupTaf.objects.get(CodeGroupTaf__exact=Gta, Company=request.user.is_company)
                    ,UserSabt = request.user ,Company = Company.objects.get(pk=request.user.is_company.pk)
                    , DateSabt=now())
                # if frm.is_valid():
                frm.save()
                return JsonResponse({'msg':'success'})
                # else:
                #     print(frm.errors)
                #     return JsonResponse({'msg':'error in saving'})    
                

        else:
            return JsonResponse({'msg':'error in loading ajax...'})
