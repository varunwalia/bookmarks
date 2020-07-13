from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'events'

urlpatterns = [
	path('create_event', views.event_creation, name='event_creation'),
	path('<int:id>/',
         views.event_detail, name='event_detail'),
]