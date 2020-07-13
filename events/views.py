from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe

from .forms import EventForm , Invitation
from .models import Event,Invite
from  .utils import Calendar

from datetime import datetime
# Create your views here.


@login_required
def dashboard(request):
	events = Event.objects.filter(user=request.user)
	invites = Invite.objects.filter(user=request.user)
	cal = Calendar(request.user,datetime.now().year,datetime.now().month)
	html_cal = cal.formatmonth(withyear=True)
	context = { 'events':events, 'invites':invites , 'calender':mark_safe(html_cal) }
	
	return render(request,'events/dashboard.html',context)	


@login_required
def event_creation(request):
	if request.method=='POST':
		form = EventForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			print(data)
			new_event = Event(user=request.user,title=data['title'],date_of_happening=data['date'],description=data['description'])
			new_event.save()
			return HttpResponseRedirect('')
	else:
		form = EventForm()
	return render(request,'events/event_form.html',{'form':form})	



@login_required
def event_detail(request,id):
	event = get_object_or_404(Event,pk=id)
	form = Invitation(user=event.user,event=event)
	count = len(event.invited_to.all()) 
	flag = False

	if count>=10:
		flag = True
	if request.method=='POST':
		form = Invitation(request.POST,user=event.user , event=event)
		if form.is_valid():
			data       = form.cleaned_data 
			new_invite = Invite(invited_to=event, user=data['customer'])
			new_invite.save()
			return HttpResponseRedirect('')
	else:
		form = Invitation(user=event.user,event=event)
	return render(request,'events/detail.html',{'event':event,'form':form , 'flag':flag})


		

