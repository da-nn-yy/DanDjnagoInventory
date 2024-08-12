from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
          product_id: 'Product ID',
          name: 'Product Name',
          sku: 'SKU',
          price: 'Price',
          quantity: 'Quantity',
          suplier: 'Suplier',  
        }
        widgets = {
          'product_id' : forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
          'name' : forms.TextInput(attrs={'placeholder':'e.g Danny', 'class':'form-control'}),
          'sku' : forms.TextInput(attrs={'placeholder':'e.g 4141dan', 'class':'form-control'}),
          'price' : forms.NumberInput(attrs={'placeholder':'e.g 200', 'class':'form-control'}),
          'quantity' : forms.NumberInput(attrs={'placeholder':'e.g 3', 'class':'form-control'}),
          'suplier' : forms.TextInput(attrs={'placeholder':'e.g Daniel', 'class':'form-control'}),
        }