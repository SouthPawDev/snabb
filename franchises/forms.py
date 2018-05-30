from django import forms
from .models import Franchise


class FranchiseForm(forms.ModelForm):

    class Meta():
        model = Franchise
        fields = ('name', 'location', 'phone_number')
