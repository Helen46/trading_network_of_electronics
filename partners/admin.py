from django.contrib import admin

from partners.models import Partner, Product

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'provider', 'country', 'city')
    search_fields = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'owner')
