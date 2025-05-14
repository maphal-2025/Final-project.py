from django.db import models

class Livestock(models.Model):
    name = models.CharField(max_length=100)
    rfid_tag = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    health_status = models.CharField(max_length=200)
    last_checkup = models.DateField()

    def __str__(self):
        return self.name