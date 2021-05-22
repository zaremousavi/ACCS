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