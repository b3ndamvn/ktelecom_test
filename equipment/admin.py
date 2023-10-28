from django.contrib import admin
from .models import Equipment, EquipmentType


class EquipmentAdmin(admin.ModelAdmin):
    pass


class EquipmentTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
