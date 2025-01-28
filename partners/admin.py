from django.contrib import admin

from partners.models import Partner, PartnerContacts


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')


@admin.register(PartnerContacts)
class PartnerContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'country')