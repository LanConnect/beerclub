from django import forms

class UserForm(forms.Form):
	person_barcode = forms.CharField()

class DrinkForm(forms.Form):
	drink_barcode = forms.CharField()

