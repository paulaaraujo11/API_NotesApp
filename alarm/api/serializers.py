from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from alarm.models import Alarm


class AlarmSerializer(ModelSerializer):
    class Meta:
        model = Alarm
        fields = ('id','time_go','time_break','time_longbreak','enabled')