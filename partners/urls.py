from rest_framework.routers import SimpleRouter

from partners.apps import PartnersConfig
from partners.views import PartnerViewSet

app_name = PartnersConfig.name

router = SimpleRouter()
router.register(r'', PartnerViewSet, basename='partners')

urlpatterns = []

urlpatterns += router.urls
