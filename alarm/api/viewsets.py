from rest_framework import viewsets
from alarm.models import Alarm
from alarm.api.serializers import AlarmSerializer

class AlarmViewSet(viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer