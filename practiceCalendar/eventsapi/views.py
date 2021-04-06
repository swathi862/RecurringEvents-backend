from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event

from django.http import HttpResponse
from dateutil.rrule import rrule, YEARLY, MONTHLY, WEEKLY, DAILY
from datetime import datetime

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('start')
    serializer_class = EventSerializer