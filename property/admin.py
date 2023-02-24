from django.contrib import admin

from .models import Complaint
from .models import Flat
from .models import Owner


class OwnershipInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'town',
        'address',
        'price',
    )
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('likes',)
    inlines = [OwnershipInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
