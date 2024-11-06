from django import forms


class CheckoutForm(forms.Form):
    address = forms.CharField()
    
