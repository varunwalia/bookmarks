from rest_framework import serializers
from  ..models import Event , Invite

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields =['id','user','title','date_of_happening','description']


class InviteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Invite
		fields =['id','invited_to','user']

