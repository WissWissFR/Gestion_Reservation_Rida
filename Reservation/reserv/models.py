from django.db import models
from django.contrib.auth.models import User

class Evenement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default=None, null=True)
    
    # class Meta:
    #     app_label = 'reserv'

class Ecole(models.Model):
    nom = models.CharField(max_length=100)

class Reservation(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
