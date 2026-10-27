from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'priority']
        # Bootstrap's form-control class styles the inputs.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'priority': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
