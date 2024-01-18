# forms.py
from django import forms
from .models import ProductDetails

class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = ['Name', 'Price', 'Description', 'Storagespace', 'Stock', 'Imagename']



class BookingForm(forms.Form):
    # Define fields for booking, for example:
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    quantity = forms.IntegerField(min_value=1, label='Quantity')