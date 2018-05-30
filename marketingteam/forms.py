from django import forms
from .models import Smr


class ImageUploadForm(forms.ModelForm):

    image = forms.ImageField()
