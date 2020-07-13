from django import forms
from django.contrib.auth.models import User
from django.db.models import Count
import datetime
from .models import Event , Invite

class EventForm(forms.Form):
	title = forms.CharField(max_length=200)
	date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
	description = forms.CharField(max_length=300 , widget=forms.Textarea)	

	def clean_date(self):
		date = self.cleaned_data['date']
		if date < datetime.date.today():
		    raise forms.ValidationError("The date cannot be in the past!")
		if date and Event.objects.get(date_of_happening=date):
			raise forms.ValidationError("You already have an event for this date")
		return date


class Invitation(forms.Form):
	def __init__(self,*args,**kwargs):
		self.user = kwargs.pop('user')
		self.event = kwargs.pop('event')
		super().__init__(*args,**kwargs)
		invites_queryset = self.event.invited_to.all()
		guests = [self.user]
		for u in invites_queryset:
			guests.append(u.user)
		queryset = User.objects.exclude(username__in=guests)
		self.fields['customer'].widget = forms.Select()
		self.fields['customer'].queryset = queryset

	customer = forms.ModelChoiceField(queryset=None)
