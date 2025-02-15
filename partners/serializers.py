from rest_framework.serializers import ModelSerializer

from partners.models import Partner


class PartnerSerializer(ModelSerializer):

    class Meta:
        model = Partner
        fields = '__all__'
        read_only_fields = ('amount_credit',)
