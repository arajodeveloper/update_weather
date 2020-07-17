from .models import Temp
from rest_framework import serializers


class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temp
        fields = ['city', 'temp', 'date']