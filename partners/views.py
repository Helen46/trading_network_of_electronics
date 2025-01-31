from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from partners.models import Partner
from partners.serializers import PartnerSerializer
from users.permissions import IsOwner, IsAdmin


class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_backends = [OrderingFilter, ]
    ordering_fields = ['country', ]

    def perform_create(self, serializer):
        partner = serializer.save()
        partner.owner = self.request.user
        partner.save()

    def get_permissions(self):
        if self.action in ('create', 'list', 'retrieve'):
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsOwner | IsAdmin,)

        return super().get_permissions()
