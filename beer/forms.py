from django.forms import *

from beer.models import *

class ParticipantForm(Form):
	barcode = CharField()

	def clean_barcode(self):
		"called on form validation"
		barcode = self.cleaned_data.get('barcode')
		if Participant.objects.filter(ident=barcode).exists():
			return barcode
		else:
			raise ValidationError('Unrecognized Barcode')

class DrinkForm(Form):
	barcode = CharField()

	def clean_barcode(self):
		"called on form validation"
		barcode = self.cleaned_data.get('barcode')
		if Drink.objects.filter(barcode=barcode).exists():
			return barcode
		else:
			raise ValidationError('Unrecognized Barcode')

class MyDrinkForm(Form):
	barcode = CharField()
	
	def clean_barcode(self):
		"called on form validation"
		barcode = self.cleaned_data.get('barcode')
		if Participant.objects.filter(ident=barcode).exists():
			return barcode
		else:
			raise ValidationError('Unrecognized Barcode')


