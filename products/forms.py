from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'discription',
            'price'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField()
    discription = forms.CharField()
    price       = forms.DecimalField()