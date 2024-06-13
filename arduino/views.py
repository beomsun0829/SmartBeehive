from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from datetime import datetime
from django.db.models import Avg, Count
from django.db.models.functions import TruncMinute

from .serializers import SoundSensorSerializer, TemperatureSensorSerializer
from .models import SoundSensor, TemperatureSensor
from .utils import calculate_q1_q3_iqr

class SoundSensorView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        
        pages = request.query_params.get('pages', None)
        if pages:
            paginator.page_size = pages
        
        sound = SoundSensor.objects.annotate(
            interval=TruncMinute('recorded_at')
        ).values('interval').annotate(
            avg_sound=Avg('sound'),
            count=Count('id')
        ).order_by('-interval')

        aggregated_sound = list(sound)

        # Extract avg_sound values for Q1, Q3, and IQR calculation
        avg_sound_values = [entry['avg_sound'] for entry in aggregated_sound]
        
        if avg_sound_values:
            q1, q3, iqr = calculate_q1_q3_iqr(avg_sound_values)
            anomaly_threshold = q3 + 1.5 * iqr

            # Mark anomalies
            for entry in aggregated_sound:
                entry['is_anomaly'] = entry['avg_sound'] > anomaly_threshold

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
        
        pages = request.query_params.get('pages', None)
        if pages:
            paginator.page_size = pages
        
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

        # Extract avg_temperature values for Q1, Q3, and IQR calculation
        avg_temperature_values = [entry['avg_temperature'] for entry in aggregated_temperature]
        
        if avg_temperature_values:
            q1, q3, iqr = calculate_q1_q3_iqr(avg_temperature_values)
            anomaly_threshold = q3 + 1.5 * iqr

            # Mark anomalies
            for entry in aggregated_temperature:
                entry['is_anomaly'] = entry['avg_temperature'] > anomaly_threshold

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
