from django.urls import path
from . import views

from arduino.views import SoundSensorView, TemperatureSensorView

urlpatterns = [
    path("sound/", SoundSensorView.as_view(), name="sound"),
    path("temp/", TemperatureSensorView.as_view(), name="temperature"),
]