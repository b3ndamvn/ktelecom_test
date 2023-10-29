from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import EquipmentType, Equipment
from .serializers import EquipmentTypeSerializer, EquipmentSerializer

import re


regex_symbols = {
    'N': '0-9',
    'A': 'A-Z',
    'a': 'a-z',
    'X': 'A-Z0-9',
    'Z': '\\-_\\@',
}


class EquipmentTypeListAPIView(ListAPIView):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def create(self, request, *args, **kwargs):
        for data in request.data:
            equipment_type_object = EquipmentType.objects.filter(pk=data['equipment_type']).first()
            mask = ''
            for mask_symbol in equipment_type_object.mask:
                mask += f'[{regex_symbols.get(mask_symbol)}]' + '{1}'
            if not re.match(mask, data['serial_number']):
                return Response(status=400, data='Ошибка!')
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=201, data='Запись прошла успешно')