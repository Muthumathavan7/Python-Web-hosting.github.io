
# from django import forms
# from .models import Purchase, PurchaseItem

# class PurchaseForm(forms.ModelForm):
#     class Meta:
#         model = Purchase
#         fields = ['customer_email', 'paid_amount']

# class PurchaseItemForm(forms.ModelForm):
#     class Meta:
#         model = PurchaseItem
#         fields = ['product', 'quantity']

from django import forms
from .models import *

class BillingForm(forms.Form):
    customer_email = forms.EmailField(label="Customer Email", required=True)
    paid_amount = forms.FloatField(label="Cash Paid by Customer", min_value=0)

class ProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label="Product")
    quantity = forms.IntegerField(label="Quantity", min_value=1)

class DenominationForm(forms.Form):
    def __init__(self, *args, available_denominations=None, **kwargs):
        super().__init__(*args, **kwargs)
        if available_denominations:
            for denom in available_denominations:
                self.fields[f"denom_{denom}"] = forms.IntegerField(label=f"{denom}", min_value=0, required=False)



