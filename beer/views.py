# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response

from beer.models import *
from beer.form import *

def home(request):
	latest_drinks = Consumed.objects.all().order_by('-pub_date')[:15]
	return render_to_response('beer/home.html', {'latest_drinks':latest_drinks,})
	return HttpResponse(t.render(c))

def user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/beer/drink/' + form.person_barcode + '/')
	else:
		form = UserForm()
	return render_to_response('beer/user_action.html', {'form':form,})

def drink(request):
	if request.method == 'POST':
		form = DrinkForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/beer/')
	else:
		form = DrinkForm()
	return render_to_response('beer/drink_action.html', {'form':form,} )
