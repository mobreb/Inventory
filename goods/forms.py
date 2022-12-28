from django import forms
from .models import Item, Person


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'quantity']


class ItemCheckForm(forms.Form):
    item_id = forms.IntegerField(required=True)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'email', 'phone_number', 'street', 'postal_code', 'country']

