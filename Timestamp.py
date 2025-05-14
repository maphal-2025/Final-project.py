from django.db import models

class CropData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    pest_detected = models.BooleanField(default=False)

    def __str__(self):
        return f"Data at {self.timestamp}"