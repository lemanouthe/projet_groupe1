from django.shortcuts import render
from .models import About

# Create your views here.

donnee = About.objects.filter(status=True)
data = {
    'donnee':donnee,
}

def about(request):
    return render(request, 'pages/config/about.html', data)