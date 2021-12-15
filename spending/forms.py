from django import forms


class SpendingForm(forms.Form):
    payer = forms.CharField()
    amount = forms.FloatField()
    date = forms.DateField(required=False)
    description = forms.CharField(required=False)
