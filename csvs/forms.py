from django import forms
from .models import CsvFileUpload

class CsvForm(forms.ModelForm):
    csvfile = forms.FileField()
    name = forms.CharField()
    
    class Meta:
        model = CsvFileUpload
        fields = ('csvfile',)
