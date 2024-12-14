# forms.py
from django import forms
from .models import Customer, Product

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'customer']

    def clean_price(self):
        price=self.cleaned_data.get('price')
        if price<=0:
            raise forms.ValidationError('price must be greater than  zero')
        return price
    def clean(self):
        cleaned_data=super().clean()
        name=cleaned_data.get('home')
        description=cleaned_data.get('description')
        if name and description and name==description:
            raise forms.ValidationError('name and description cannot be same')
