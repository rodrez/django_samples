from django import forms

from rates.models import Rate


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ["data", "credit_union"]
        widgets = {
            "data": forms.HiddenInput(),
            "credit_union": forms.HiddenInput(),
        }
