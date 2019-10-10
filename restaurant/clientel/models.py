from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import datetime, date, time
import re
from resto.models import Plat

# Create your models here.
#cette classe concerne la reservation
    #quand on fait poste on doit trouver une fonctionnalite qui va dire si le nombrepersonne
    #est a ou b retirer ce nombre dans le nbre_place_disponible dans la classe place

class Reservation(models.Model):
        nom = models.CharField(max_length=160)
        email = models.EmailField()
        numero = models.CharField(max_length=160)
        date = models.DateField()
        heure = models.TimeField()
        personne = models.IntegerField()
        message = models.TextField(null=True)
        date_add =  models.DateTimeField(auto_now_add=True)
        date_update =  models.DateTimeField(auto_now=True)
        status =  models.BooleanField(default=True)
        
        def __str__(self):
            return self.nom

        class Meta:
            verbose_name = 'Reservation'
            verbose_name_plural = 'Reservations'
            
    #ici le champs par defaut comme metier des temoins est client 


class Temoignage(models.Model):
        nom = models.CharField(max_length=160)
        commentaire = models.TextField()
        image = models.ImageField(upload_to='client/testimonial')
        job = models.CharField(max_length=255)
        #social = ManyToManyField(Social,related_name='social_testimonial')#cette ligne depend du model de testimonial choisie
        date_add =  models.DateTimeField(auto_now_add=True)
        date_update =  models.DateTimeField(auto_now=True)
        status =  models.BooleanField(default=True)
        
        def __str__(self):
            return self.nom

        class Meta:
            verbose_name = 'Temoignage'
            verbose_name_plural = 'Temoignages'