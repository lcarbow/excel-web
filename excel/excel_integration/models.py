from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    #termin = models.DateTimeField()
    termin = models.CharField(max_length=100)
    vorname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    straße = models.CharField(max_length=100)
    hausnummer = models.CharField(max_length=10)
    plz = models.CharField(max_length=10)
    stadt = models.CharField(max_length=100)
    telefon_primär = models.CharField(max_length=20)
    telefon_sekundär = models.CharField(max_length=20)
    email = models.EmailField()
    objekt = models.CharField(max_length=100)
    anlage = models.CharField(max_length=100)
    dach = models.CharField(max_length=100)
    infos = models.TextField()
    speicher = models.TextField(max_length=100)
    interesse = models.TextField(max_length=100)
    jährlicher_stromverbrauch = models.TextField(max_length=100)
    anfrage_über = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    kunden_id = models.PositiveIntegerField(unique=True)
    
    # def __str__(self):
    #     return f"{self.vorname} {self.name}"




# Create your models here.

# termin = models.DateField()
#     vorname = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     straße = models.CharField(max_length=100)
#     hausnummer = models.CharField(max_length=10)
#     plz = models.CharField(max_length=10)
#     stadt = models.CharField(max_length=100)
#     telefon_primär = models.CharField(max_length=20)
#     telefon_sekundär = models.CharField(max_length=20)
#     email = models.EmailField()
#     objekt = models.CharField(max_length=100)
#     anlage = models.CharField(max_length=100)
#     dach = models.CharField(max_length=100)
#     infos = models.TextField()
#     speicher = models.BooleanField(default=False)
#     interesse = models.BooleanField(default=False)
#     jährlicher_stromverbrauch = models.DecimalField(max_digits=10, decimal_places=2)
#     anfrage_über = models.CharField(max_length=100)
#     kunden_id = models.CharField(max_length=100, blank=True, null=True)
