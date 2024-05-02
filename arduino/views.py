from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

from .serializers import SoundSensorSerializer, TemperatureSensorSerializer
from .models import SoundSensor, TemperatureSensor

class SoundSensorView(APIView):
    def get(self, request):
        sound = SoundSensor.objects.all()
        serializer = SoundSensorSerializer(sound, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        #serializer = SoundSensorSerializer(data=request.data)
        
        recorded_at = datetime.strptime(request.data["timestamp"], "%Y-%m-%d %H:%M:%S")
        sound = request.data["sound"]

        SoundSensor.objects.create(sound=sound, recorded_at=recorded_at).save()
        return Response({"status": "success"}, status=200)

        # serializer = SoundSensorSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"status": "success"}, status=201)
        # else:
        #     return Response({"status": "failed"}, status=400)
        
class TemperatureSensorView(APIView):
    def get(self, request):
        temperature = TemperatureSensor.objects.all()
        serializer = TemperatureSensorSerializer(temperature, many=True)    
        return Response(serializer.data)

    def post(self, request):
        #serializer = TemperatureSensorSerializer(data=request.data)
        
        recorded_at = datetime.strptime(request.data["timestamp"], "%Y-%m-%d %H:%M:%S")
        co = request.data["co"]
        temperature = request.data["temperature"]
        humidity = request.data["humidity"]
        nitrogen_dioxide = request.data["nitrogen_dioxide"]

        TemperatureSensor.objects.create(co = co , temperature = temperature , humidity = humidity , nitrogen_dioxide= nitrogen_dioxide , recorded_at=recorded_at).save()
        return Response({"status": "success"}, status=200)

        # serializer = TemperatureSensorSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"status": "success"}, status=201)
        # else:
        #     return Response({"status": "failed"}, status=400)