from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('nom', 'email', 'numero', 'date', 'heure', 'personne', 'message')