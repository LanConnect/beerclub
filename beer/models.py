from django.db import models

SPEC_GRAV_ETHANOL = 0.789

# Create your models here.

class Participant(models.Model):
	name = models.CharField(max_length=255)
	#Something like a barcode?
	ident = models.CharField(max_length=255, unique=True)
	def __unicode__(self):
		return self.name

class Drink(models.Model):
	name = models.CharField(max_length=200)
	percent_alc = models.IntegerField('Percent Alcohol', help_text='By volume')
	volume = models.IntegerField(help_text='in mL')
	location = models.CharField(max_length=100)
	cost = models.IntegerField()
	stock = models.IntegerField()
	barcode = models.CharField(max_length=100, unique=True)
	def standard_drinks(self):
		return self.volume/1000.0 * self.percent_alc * SPEC_GRAC_ETHANOL
	def __unicode__(self):
		return self.name

class Consumed(models.Model):
	participant = models.ForeignKey(Participant)
	drink = models.ForeignKey(Drink)
	pub_date = models.DateTimeField('date drunk', auto_now_add=True)
	def __unicode__(self):
		if self.drink.name[0].lower() in 'aeiou':
			return self.participant.name + ' drank an ' + self.drink.name
		else:
			return self.participant.name + ' drank a ' + self.drink.name

class Tab(models.Model):
	balance = models.IntegerField(default=0)
	participant = models.ForeignKey(Participant)
	def __unicode__(self):
		return "%s: $%.2f" % (self.participant.name, self.balance)

