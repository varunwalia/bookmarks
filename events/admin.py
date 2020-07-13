from django.contrib import admin
from .models import Event , Invite
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('user','title','date_of_happening','description')

admin.site.register(Invite)
# class EventAdmin(admin.ModelAdmin):
# 	list_display = ('invited_to',)