from django.db import models

# Create your models here.

class Participant(models.Model):
	name = models.CharField(max_length=255)
	#Something like a barcode?
	ident = models.CharField(max_length=255, unique=True)
	def __unicode__(self):
		return self.name

class Drink(models.Model):
	name = models.CharField(max_length=200)
	percent_alc = models.IntegerField()
	volume = models.IntegerField()
	location = models.CharField(max_length=100)
	cost = models.IntegerField()
	stock = models.IntegerField()
	barcode = models.CharField(max_length=100, unique=True)
	def __unicode__(self):
		return self.name

class Consumed(models.Model):
	participant = models.ForeignKey(Participant)
	drink = models.ForeignKey(Drink)
	pub_date = models.DateTimeField('date drunk')
	def __unicode__(self):
		return self.participant.name + ' - ' + self.drink.name

class Tab(models.Model):
	balance = models.IntegerField()
	participant = models.ForeignKey(Participant)
	def __unicode__(self):
		return self.participant.name

