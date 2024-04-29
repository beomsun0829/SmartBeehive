from rest_framework import serializers
from .models import SoundSensor, TemperatureSensor

class SoundSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundSensor
        fields = "__all__"
        extra_kwargs = {
            'recorded_at':{
                'format': '%m-%d %H:%M:%S',
                'input_formats': ['%m-%d %H:%M:%S']
            }
        }

class TemperatureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureSensor
        fields = "__all__"
        extra_kwargs = {
            'recorded_at':{
                'format': '%Y-%m-%d %H:%M',
                'input_formats': ['%Y-%m-%d %H:%M']
            }
        }
        
