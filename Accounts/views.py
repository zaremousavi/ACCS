from django.shortcuts import render
from .models import GroupAcc, KolAcc, MoinAcc, GroupTaf, Tafsili
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormValidMixin, FieldMixin, FieldKolMixin, FormValidKolMixin, FieldMoinMixin, FormValidMoinMixin, \
    AccessMixin
from .mixins import AccessKolMixin, AccessMoinMixin, AccessGroupTafMixin, FieldGroupTafMixin, FormValidGroupTafMixin
from .mixins import FormValidTafsiliMixin, AccessTafsiliMixin, FieldTafsiliMixin

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