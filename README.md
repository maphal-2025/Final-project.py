# Final-project.py

pip install django flask requests pandas numpy tensorflow firebase-admin stripe googlemaps

python -m venv agritech_env
agritech_env\Scripts\activate  # (Windows)

django-admin startproject agritech
cd agritech
python manage.py runserver

mkdir flask_app && cd flask_app
touch app.py

pip install google-cloud-vision googlemaps

git init
git add .
git commit -m "https://github.com/goauthentik/authentik.git"

git remote add origin https://github.com/maphal-2025/your_repo.git
git push -u origin main

django-admin startproject crop_monitoring
cd crop_monitoring
django-admin startapp crops

from django.db import models

class CropData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    pest_detected = models.BooleanField(default=False)

    def __str__(self):
        return f"Data at {self.timestamp}"

from django.shortcuts import render
from django.http import JsonResponse
from .models import CropData

def get_crop_data(request):
    data = CropData.objects.all().order_by('-timestamp')[:10]
    response = [{"timestamp": d.timestamp, "temp": d.temperature, "humidity": d.humidity, "moisture": d.soil_moisture, "pest_detected": d.pest_detected} for d in data]
    return JsonResponse(response, safe=False)

django-admin startproject livestock_manager
cd livestock_manager
django-admin startapp livestock

from django.db import models

class Livestock(models.Model):
    name = models.CharField(max_length=100)
    rfid_tag = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    health_status = models.CharField(max_length=200)
    last_checkup = models.DateField()

    def __str__(self):
        return self.name

from django.shortcuts import render
from django.http import JsonResponse
from .models import Livestock

def get_livestock_data(request):
    livestock_data = Livestock.objects.all()
    response = [{"Mary": l.name, "2515": l.rfid_tag, "3": l.age, "health_status": l.health_status, "10/05/2025": l.last_checkup} for l in livestock_data]
    return JsonResponse(response, safe=False)

django-admin startproject agri_marketplace
cd agri_marketplace
django-admin startapp marketplace

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def get_products(request):
    products = Product.objects.all()
    response = [{"Mary": p.name, "Kettle": p.category, "R10000": p.price, "livestock star": p.supplier, "4.5": p.rating} for p in products]
    return JsonResponse(response, safe=False)

npx create-react-app agritech-frontend
cd agritech-frontend
npm start

npm install axios

import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [cropData, setCropData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/get_crop_data")
      .then(response => setCropData(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Crop Monitoring System</h1>
      <ul>
        {cropData.map((data, index) => (
          <li key={index}>Temp: {data.temp}, Humidity: {data.humidity}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

npm start

pip install django-cors-headers

INSTALLED_APPS = [
    "corsheaders",
    "rest_framework",
    ...
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Allow requests from React frontend
]

pip install djangorestframework-simplejwt

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

    FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000

docker build -t agritech-backend .
docker run -p 8000:8000 agritech-backend

sudo apt update
sudo apt install python3-pip python3-venv nginx

gunicorn --bind 0.0.0.0:8000 crop_monitoring.wsgi

pip install djangorestframework-simplejwt

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.http import JsonResponse

def generate_tokens(request, username):
    user = User.objects.get(username=username)
    refresh = RefreshToken.for_user(user)
    return JsonResponse({'access': str(refresh.access_token), 'refresh': str(refresh)})

npm install bootstrap

import "bootstrap/dist/css/bootstrap.min.css";

<div className="container">
  <h1 className="text-center text-primary">Crop Monitoring Dashboard</h1>
</div>

























