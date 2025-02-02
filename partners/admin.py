from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from partners.models import Partner, Product

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'country', 'city', 'provider_link', 'amount_credit')
    search_fields = ('city',)
    actions = ('clear_amount_credit',)

    @admin.display(description='поставщик')
    def provider_link(self, obj):
        if obj.provider is not None:
            return format_html(
                f'<a href="/admin/partners/partner/{obj.provider.id}/change/">{obj.provider.name}</a>'
            )
        return "-"

    provider_link.allow_tags = True

    @admin.action(description='Очистить задолженности выбранных объектов')
    def clear_amount_credit(self, request, queryset):
        queryset.update(amount_credit=0)
        self.message_user(request, f"Задолженности выбранных объектов очищены.")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'owner')
