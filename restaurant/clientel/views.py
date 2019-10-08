from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,BasePermission,SAFE_METHODS
from .serializer import ReservationSerializer, TemoignageSerializer
from .models import Reservation , Temoignage


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ReservationViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = []
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.filter(status=True)

class TemoignageViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TemoignageSerializer
    queryset = Temoignage.objects.filter(status=True)
    