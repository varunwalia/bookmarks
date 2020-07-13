from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Event(models.Model):
	user       = models.ForeignKey(User,on_delete=models.CASCADE,related_name='event_owner')
	title = models.CharField(max_length=200)
	date_of_happening = models.DateField(unique='True' ,blank=False)
	description = models.CharField(max_length=2000)
	# invites = models.ManyToManyField(Invite , related_name='invites')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('events:event_detail',
					args=[self.id])

class Invite(models.Model):
	invited_to       = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='invited_to')
	user             = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')

	def __str__(self):
		return self.invited_to.title



