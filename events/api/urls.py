from django.urls import path,include
from rest_framework import routers
from . import views
 

router=routers.DefaultRouter()
router.register('events' , views.EventViewSet)
router.register('invite' , views.InviteViewSet)
 
app_name = 'events'
 
urlpatterns = [

	path("",include(router.urls)),

]