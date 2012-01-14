# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render

from beer.models import *
from beer.forms import *

def home(request):
	latest_drinks = Consumed.objects.all().order_by('-pub_date')[:15]
	return render(request, 'beer/home.html', {'latest_drinks':latest_drinks,})
	return HttpResponse(t.render(c))

def user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/beer/drink/%s/' % form.cleaned_data.get('barcode'))
	else:
		form = UserForm()
	return render(request, 'beer/user_action.html', {'form':form,})

def drink(request, user_barcode):
	if request.method == 'POST':
		form = DrinkForm(request.POST)
		if form.is_valid():
			participant = Participant.objects.get(ident=user_barcode)
			drink = Drink.objects.get(barcode = form.cleaned_data.get('barcode'))
			Consumed.objects.create(participant=participant, drink=drink)
			tab, created = Tab.objects.get_or_create(participant=participant)
			tab.balance -= drink.cost ; tab.save()
                        drink.stock -=1 ; drink.save()
			return HttpResponseRedirect('/beer/')
	else:
		form = DrinkForm()
	return render(request, 'beer/drink_action.html', {'form':form,} )
