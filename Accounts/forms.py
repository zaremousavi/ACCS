from django.forms import ModelForm
from .models import MoinTafRel

class MoinTafRelForm(ModelForm):
    class Meta:
        model = MoinTafRel
        fields = ['Moin','Level','GroupTaf', 'UserSabt', 'DateSabt','Company']