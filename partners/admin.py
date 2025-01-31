from django.contrib import admin

from partners.models import Partner, Product, Credit

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'provider', 'country', 'city')
    search_fields = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'owner')


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'creditor', 'debtor')