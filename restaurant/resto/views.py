from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'pages/resto/index.html')

def menu(request):

    return render(request, 'pages/resto/menu.html')

def special_dishes(request):

    return render(request, 'pages/resto/special_dishes.html')

def team(request):

    return render(request, 'pages/resto/team.html')