from rest_framework import viewsets ,filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,BasePermission,SAFE_METHODS
from .serializer import NewsletterSerializer , MessageSerializer
from .models import Newsletter , Message



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
# Create your views here.

class NewsletterViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [IsAdminUser]
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()

class MessageViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [IsAdminUser]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
