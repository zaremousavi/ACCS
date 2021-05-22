from django import forms
from .models import VoucherDTL


class VoucherDTLForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        pass
