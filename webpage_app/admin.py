from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from webpage_app.models import Purchaser, Manufacturer, BearingCategory, BearingType


@admin.register(Purchaser)
class PurchaserAdmin(UserAdmin):
    pass


@admin.register(Manufacturer)
class PurchaserAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("produce_bearing_type", "responsible_purchaser")


admin.site.register(BearingType)

admin.site.register(BearingCategory)

admin.site.unregister(Group)
