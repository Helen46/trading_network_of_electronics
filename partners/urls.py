from django.urls import path
from rest_framework.routers import SimpleRouter

from partners.apps import PartnersConfig
from partners.views import PartnerViewSet, PartnerContactsListApiView, PartnerContactsCreateApiView, \
    PartnerContactsRetrieveApiView, PartnerContactsUpdateApiView, PartnerContactsDestroyApiView

app_name = PartnersConfig.name

router = SimpleRouter()
router.register(r'', PartnerViewSet, basename='partners')

urlpatterns = [
    path('contacts/', PartnerContactsListApiView.as_view(), name='contacts_list'),
    path('contacts/create/', PartnerContactsCreateApiView.as_view(), name='contacts_create'),
    path('contacts/<int:pk>/', PartnerContactsRetrieveApiView.as_view(), name='contacts_retrieve'),
    path('contacts/update/<int:pk>/', PartnerContactsUpdateApiView.as_view(), name='contacts_update'),
    path('contacts/delete/<int:pk>/', PartnerContactsDestroyApiView.as_view(), name='contacts_delete'),
]

urlpatterns += router.urls
