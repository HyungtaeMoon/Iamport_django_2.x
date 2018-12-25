from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', 'name', 'amount']

    list_display_links = ['name']

    def photo_tag(self, item):
        if item.photo:
            return mark_safe('<img src={} style="width: 75px;"/>'.format(item.photo.url))
        return None


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'merchant_uid', 'imp_uid', 'name', 'status', 'created_at']

    list_display_links = ['id', 'merchant_uid']
