from django.shortcuts import render
from django.http import JsonResponse
from .models import CropData

def get_crop_data(request):
    data = CropData.objects.all().order_by('-timestamp')[:10]
    response = [{"timestamp": d.timestamp, "temp": d.temperature, "humidity": d.humidity, "moisture": d.soil_moisture, "pest_detected": d.pest_detected} for d in data]
    return JsonResponse(response, safe=False)