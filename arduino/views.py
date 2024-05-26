from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from datetime import datetime
from django.db.models import Avg, Count
from django.db.models.functions import TruncMinute

from .serializers import SoundSensorSerializer, TemperatureSensorSerializer
from .models import SoundSensor, TemperatureSensor

class SoundSensorView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        
        sound = SoundSensor.objects.annotate(
            interval=TruncMinute('recorded_at')
        ).values('interval').annotate(
            avg_sound=Avg('sound'),
            count=Count('id')
        ).order_by('-interval')

        aggregated_sound = list(sound)
        result_page = paginator.paginate_queryset(aggregated_sound, request)
        
        return paginator.get_paginated_response(result_page)
    
    def post(self, request):
        recorded_at = datetime.strptime(request.data["timestamp"], "%Y-%m-%d %H:%M:%S")
        sound = request.data["sound"]

        SoundSensor.objects.create(sound=sound, recorded_at=recorded_at).save()
        return Response({"status": "success"}, status=200)
        
class TemperatureSensorView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        
        temperature = TemperatureSensor.objects.annotate(
            interval=TruncMinute('recorded_at')
        ).values('interval').annotate(
            avg_temperature=Avg('temperature'),
            avg_co=Avg('co'),
            avg_humidity=Avg('humidity'),
            avg_nitrogen_dioxide=Avg('nitrogen_dioxide'),
            count=Count('id')
        ).order_by('-interval')

        aggregated_temperature = list(temperature)
        result_page = paginator.paginate_queryset(aggregated_temperature, request)
        
        return paginator.get_paginated_response(result_page)

    def post(self, request):
        recorded_at = datetime.strptime(request.data["timestamp"], "%Y-%m-%d %H:%M:%S")
        co = request.data["co"]
        temperature = request.data["temperature"]
        humidity = request.data["humidity"]
        nitrogen_dioxide = request.data["nitrogen_dioxide"]

        TemperatureSensor.objects.create(co=co, temperature=temperature, humidity=humidity, nitrogen_dioxide=nitrogen_dioxide, recorded_at=recorded_at).save()
        return Response({"status": "success"}, status=200)
