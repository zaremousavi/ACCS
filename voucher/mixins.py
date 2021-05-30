from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import VoucherDTL, VoucherHDR

class FormValidMixinVoucherDTL():
    def form_valid(self, form):
        # if self.request.user.is_company_active:
        #     form.save()
        # else:
        self.obj = form.save(commit=False)
        self.obj.Company = self.request.user.is_company
        self.obj.UserSabt = self.request.user
        self.obj.save()
        return super().form_valid(form)

class FieldMixinVoucherDTL():
    def dispatch(self, request, *args, **kwargs):
        self.fields= ['CodeKol', 'CodeMoin', 'Taf1', 'Taf2', 'Taf3', 'Taf4', 'Disc', 'Debit', 'Credit']
        return super().dispatch(request, *args, **kwargs)
    





# class FieldMixin():
#     def dispatch(self, request, *args, **kwargs):
#         self.fields = ['CodeGroup', 'TitleGroup', 'kind']
#         return super().dispatch(request, *args, **kwargs)

# class FormValidMixin():
#     def form_valid(self, form):
#         # if self.request.user.is_company_active:
#         #     form.save()
#         # else:
#         self.obj = form.save(commit=False)
#         self.obj.Company = self.request.user.is_company
#         self.obj.UserSabt = self.request.user
#         self.obj.save()
#         return super().form_valid(form)

# class AccessMixin():
#     def dispatch(self, request, pk , *args, **kwargs):
#         GrAcc = get_object_or_404(GroupAcc, pk=pk)
#         if GrAcc.UserSabt == request.user:
#             return super().dispatch(request, *args, **kwargs)
