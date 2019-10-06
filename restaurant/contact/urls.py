
from django.urls import path
from .models import Message , Newsletter
from .views import MessageViewset, NewsletterViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'message',MessageViewset,base_name='messages')
router.register(r'newsletter',NewsletterViewset,base_name='newsletters')
urlpatterns = [
    
]

urlpatterns += router.urls