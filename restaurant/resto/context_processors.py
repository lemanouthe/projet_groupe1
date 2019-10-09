from django.conf import settings
from configuration.models import  Day, WorkingHour, Presentation, Social

def horaire(request):
    horaires = WorkingHour.objects.all()[:7]
    presentation = Presentation.objects.filter(status=True)[:1]
    social = Social.objects.filter(status=True)
    return {'horaires': horaires, 'presentation': presentation, 'social':social }