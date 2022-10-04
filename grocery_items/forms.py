from django import forms 

class ItemForm(forms.Form):
    item = forms.CharField(max_length=100)
    brand = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)
    price = forms.CharField(max_length=100, required=False)
    price_type = forms.CharField(max_length=100, required=False)
    servings = forms.CharField(max_length=100, required=False)
    
