from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from api_with_restrictions.permissions import IsOwnerOrReadOnly
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all().order_by('-updated_at')
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        if self.action == 'delete':
            return [IsOwnerOrReadOnly()]
        return []
