from django.shortcuts import render
from django.http import JsonResponse
from .models import Livestock

def get_livestock_data(request):
    livestock_data = Livestock.objects.all()
    response = [{"Mary": l.name, "4215": l.rfid_tag, "3": l.age, "Good": l.health_status, "10/05/2025": l.last_checkup} for l in livestock_data]
    return JsonResponse(response, safe=False)