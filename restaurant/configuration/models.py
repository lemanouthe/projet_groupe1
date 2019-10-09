from django.db import models
from django.utils.timezone import now
from datetime import datetime, date, time
import re
# Create your models here.

class Day(models.Model):
    # TODO: Define fields here
    jour = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Days"

    def __str__(self):
        return '{}'.format(self.jour)

class WorkingHour(models.Model):
    # TODO: Define fields here
    jour = models.ForeignKey(Day,on_delete=models.CASCADE,related_name='day_working')
    start_hour = models.TimeField(max_length=50)
    end_hour = models.TimeField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "WorkingHour"
        verbose_name_plural = "WorkingHours"

    def __str__(self):
        return '{}  {} - {}'.format(self.jour,self.start_hour,self.end_hour)

class Presentation(models.Model):
    """Model definition for Presentation."""

    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image_accueil', )
    text_accueil = models.TextField()
    lien_video = models.URLField(max_length=255)
    text1 = models.CharField(max_length=255)
    text2 = models.CharField(max_length=255)
    text3 = models.CharField(max_length=255)
    working_hour = models.ManyToManyField('WorkingHour',related_name='working_config')
    license_site = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_udp =  models.DateTimeField(auto_now =True)

    @property
    def open_hour(self):
        jour = now().strftime('%A')
        hour = ''
        for w in self.working_hour.all():
            if re.match(str(w.jour),str(jour),re.IGNORECASE):
                hour = '{} - {}'.format(str(w.start_hour),str(w.end_hour))
        print(jour,' : ',hour)
        return '{} : {}'.format(jour,hour)

    class Meta:
        """Meta definition for Presentation."""

        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        """Unicode representation of Presentation."""
        return self.nom


#cette classe concerne tout ce qui est dans la partie about.html et qui se repete dans le home

class About(models.Model):
    """Model definition for About."""

    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image_about')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_udp =  models.DateTimeField(auto_now =True)

    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        """Unicode representation of About."""
        return self.nom


class Social(models.Model):
    # TODO: Define fields here
    choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
    name = models.CharField(max_length=100,choices=choice)
    lien = models.URLField(max_length=200)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    @property
    def font(self):
        if self.name == 'FB':
            font = 'icon-facebook'
        elif self.name == 'TW':
            font ='icon-twitter'
        elif self.name == 'INS':
            font ='icon-instagram"'
        elif self.name == 'GOO':
            font ='icon-google-plus'
        return font
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

    def __str__(self):
        return '{}'.format(self.name)

class ReserveConfig(models.Model):
    """Model definition for ReserveConfiguration."""

    titre = models.CharField(max_length=255)
    sous_titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='resrvation')
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_udp =  models.DateTimeField(auto_now =True)

    
    # TODO: Define fields here

    class Meta:
        """Meta definition for ReserveConfiguration."""

        verbose_name = 'ReserveConfig'
        verbose_name_plural = 'ReserveConfig'
