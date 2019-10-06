from rest_framework import viewsets
from .serializer import NewsletterSerializer , MessageSerializer
from .models import Newsletter , Message

# Create your views here.

class NewsletterViewset(viewsets.ModelViewSet):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()

class MessageViewset(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
