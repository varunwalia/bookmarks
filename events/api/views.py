from rest_framework import generics , viewsets
from rest_framework.authentication import BasicAuthentication


from ..models import Event , Invite
from .serializers import EventSerializer , InviteSerializer


from rest_framework import permissions



class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class =EventSerializer
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		user_queryset = self.queryset.filter(user=self.request.user)
		return user_queryset
		

class InviteViewSet(viewsets.ModelViewSet):
	queryset = Invite.objects.all()
	serializer_class =InviteSerializer
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		user_queryset = self.queryset.filter(user=self.request.user)
		return user_queryset





