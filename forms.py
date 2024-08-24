from django import forms
from main.models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"
        widgets = {
            'mail': forms.TextInput(attrs={'class': 'form-control'})
        }
