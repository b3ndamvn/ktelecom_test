from django.db import models
from django.core.validators import RegexValidator


class EquipmentType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    mask = models.CharField(max_length=10, unique=True, validators=[
        RegexValidator(
            regex='^[NAaXZ]{10}$',
            message='Неверный формат ввода',
            code='invalid_mask'
        ),
    ])

    def __str__(self):
        return self.name + ' ' + f'({self.mask})'


class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=10, unique=True)
    notice = models.TextField()
