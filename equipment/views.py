from rest_framework.viewsets import ModelViewSet
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


class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def create(self, request, *args, **kwargs):
        equipment_type_object = EquipmentType.objects.filter(pk=request.data['equipment_type']).first()
        serializer = EquipmentSerializer(data=request.data)
        mask = ''
        for mask_symbol in equipment_type_object.mask:
            mask += f'[{regex_symbols.get(mask_symbol)}]' + '{1}'
        if re.match(mask, request.data['serial_number']) and serializer.is_valid():
            serializer.save()
            return Response(status=201, data='Запись прошла успешно')
        return Response(status=400, data='Неверный формат ввода данных')

