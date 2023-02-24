from django.contrib import admin

from .models import Complaint
from .models import Flat
from .models import Owner


class OwnershipInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)

class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'id',
        'town',
        'address',
        'price',
        'owner'
    )
    readonly_fields = ['created_at']
    list_display = (
        'id',
        'address',
        'price',
        'new_building',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('likes',)
    inlines = [OwnershipInline]

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Complaint, ComplaintAdmin)
