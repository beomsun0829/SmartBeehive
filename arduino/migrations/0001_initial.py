# Generated by Django 5.0.4 on 2024-04-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SoundSensor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("sound", models.FloatField()),
                ("recorded_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="TemperatureSensor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("co", models.FloatField()),
                ("temperature", models.FloatField()),
                ("humidity", models.FloatField()),
                ("nitrogen_dioxide", models.FloatField()),
                ("recorded_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]