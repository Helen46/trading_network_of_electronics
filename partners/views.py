from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from partners.models import Partner, PartnerContacts
from partners.serializers import PartnerSerializer, PartnerContactsSerializer
from users.permissions import IsOwner, IsAdmin


class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

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


class PartnerContactsCreateApiView(CreateAPIView):
    queryset = PartnerContacts.objects.all()
    serializer_class = PartnerContactsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        partner_contacts = serializer.save()
        partner_contacts.owner = self.request.user
        partner_contacts.save()


class PartnerContactsListApiView(ListAPIView):
    queryset = PartnerContacts.objects.all()
    serializer_class = PartnerContactsSerializer
    permission_classes = (IsAuthenticated,)


class PartnerContactsRetrieveApiView(RetrieveAPIView):
    queryset = PartnerContacts.objects.all()
    serializer_class = PartnerContactsSerializer
    permission_classes = (IsAuthenticated,)


class PartnerContactsUpdateApiView(UpdateAPIView):
    queryset = PartnerContacts.objects.all()
    serializer_class = PartnerContactsSerializer
    permission_classes = (IsAdmin | IsOwner,)


class PartnerContactsDestroyApiView(DestroyAPIView):
    queryset = PartnerContacts.objects.all()
    serializer_class = PartnerContactsSerializer
    permission_classes = (IsAdmin | IsOwner,)
