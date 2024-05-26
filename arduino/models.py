from django.db import models

    
class SoundSensor(models.Model):
    id = models.AutoField(primary_key=True)
    sound = models.FloatField()
    recorded_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class TemperatureSensor(models.Model):
    id = models.AutoField(primary_key=True)
    co = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    nitrogen_dioxide = models.FloatField()
    recorded_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
