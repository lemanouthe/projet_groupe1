from django.shortcuts import render
from .models import About

# Create your views here.



def about(request):
    donnee = About.objects.filter(status=True)
    data = {
        'donnee':donnee,
    }
    return render(request, 'pages/config/about.html', data)