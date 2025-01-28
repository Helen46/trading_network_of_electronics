from rest_framework.serializers import ModelSerializer

from partners.models import Partner, PartnerContacts


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class PartnerContactsSerializer(ModelSerializer):
    class Meta:
        model = PartnerContacts
        fields = '__all__'
