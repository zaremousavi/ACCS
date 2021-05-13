from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import GroupAcc, KolAcc, MoinAcc, GroupTaf, Tafsili

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['CodeGroup', 'TitleGroup', 'kind']
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self, form):
        # if self.request.user.is_company_active:
        #     form.save()
        # else:
        self.obj = form.save(commit=False)
        self.obj.Company = self.request.user.is_company
        self.obj.UserSabt = self.request.user
        self.obj.save()
        return super().form_valid(form)

class AccessMixin():
    def dispatch(self, request, pk , *args, **kwargs):
        GrAcc = get_object_or_404(GroupAcc, pk=pk)
        if GrAcc.UserSabt == request.user:
            return super().dispatch(request, *args, **kwargs)


class AccessKolMixin():
    def dispatch(self, request, pk , *args, **kwargs):
        KlAcc = get_object_or_404(KolAcc, pk=pk)
        if KlAcc.UserSabt == request.user:
            return super().dispatch(request, *args, **kwargs)

class AccessMoinMixin():
    def dispatch(self, request, pk , *args, **kwargs):
        MoAcc = get_object_or_404(MoinAcc, pk=pk)
        if MoAcc.UserSabt == request.user:
            return super().dispatch(request, *args, **kwargs)


class FieldKolMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['CodeGroup', 'CodeKol', 'TitleKol', 'kind']
        return super().dispatch(request, *args, **kwargs)

class FormValidKolMixin():
    def form_valid(self, form):
        # if self.request.user.is_company_active:
        #     form.save()
        # else:
        self.obj = form.save(commit=False)
        self.obj.Company = self.request.user.is_company
        self.obj.UserSabt = self.request.user
        self.obj.save()
        return super().form_valid(form)


class FieldMoinMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['CodeKol', 'CodeMoin', 'TitleMoin', 'Kind', 'TafRel']
        return super().dispatch(request, *args, **kwargs)

class FormValidMoinMixin():
    def form_valid(self, form):
        # if self.request.user.is_company_active:
        #     form.save()
        # else:
        self.obj = form.save(commit=False)
        self.obj.Company = self.request.user.is_company
        self.obj.UserSabt = self.request.user
        self.obj.save()
        return super().form_valid(form)


#GroupTaf
class FieldGroupTafMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['CodeGroupTaf', 'TitleGroupTaf']

        return super().dispatch(request, *args, **kwargs)

class FormValidGroupTafMixin():
    def form_valid(self, form):
        # if self.request.user.is_company_active:
        #     form.save()
        # else:
        self.obj = form.save(commit=False)
        self.obj.Company = self.request.user.is_company
        self.obj.UserSabt = self.request.user
        self.obj.save()
        return super().form_valid(form)

class AccessGroupTafMixin():
    def dispatch(self, request, pk , *args, **kwargs):
        GrTaf = get_object_or_404(GroupTaf, pk=pk)
        if GrTaf.UserSabt == request.user:
            return super().dispatch(request, *args, **kwargs)


#tafsili
class FieldTafsiliMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['CodeTafsili', 'TitleTafsili', 'CodeGroupTaf', 'Tozihat', 'is_Active', 'is_Tax']
        return super().dispatch(request, *args, **kwargs)

class FormValidTafsiliMixin():
    def form_valid(self, form):
        # if self.request.user.is_company_active:
        #     form.save()
        # else:
        self.obj = form.save(commit=False)
        self.obj.Company = self.request.user.is_company
        self.obj.UserSabt = self.request.user
        self.obj.save()
        return super().form_valid(form)

class AccessTafsiliMixin():
    def dispatch(self, request, pk , *args, **kwargs):
        Taf = get_object_or_404(Tafsili, pk=pk)
        if Taf.UserSabt == request.user:
            return super().dispatch(request, *args, **kwargs)
