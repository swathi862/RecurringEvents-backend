from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'start', 'end', 'ical_string')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

