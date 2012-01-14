from beer.models import *
from django.contrib import admin

class DrinkAdmin(admin.ModelAdmin):
	list_display = ('name', 'location','volume', 'cost', 'stock')
	list_editable = ('stock',)

class ConsumedAdmin(admin.ModelAdmin):
	list_display = ('drink', 'participant', 'pub_date')

class TabAdmin(admin.ModelAdmin):
	list_display = ('participant', 'balance')
	list_editable = ('balance',)

class ParticipantAdmin(admin.ModelAdmin):
	pass

admin.site.register(Drink, DrinkAdmin)
admin.site.register(Consumed, ConsumedAdmin)
admin.site.register(Tab, TabAdmin)
admin.site.register(Participant, ParticipantAdmin)

