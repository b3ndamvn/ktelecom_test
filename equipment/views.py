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
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        not_valid = []
        print(request.data)
        if not isinstance(request.data, list):
            req_data = [request.data]
        else:
            req_data = request.data
        for data in req_data:
            print(data)
            equipment_type_object = EquipmentType.objects.filter(pk=data['equipment_type']).first()
            mask = ''
            for mask_symbol in equipment_type_object.mask:
                mask += f'[{regex_symbols.get(mask_symbol)}]' + '{1}'
            if not re.match(mask, data['serial_number']):
                not_valid.append(data['serial_number'])
                continue
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        if not not_valid:
            return Response(status=201, data='Запись прошла успешно')
        if len(not_valid) == len(request.data):
            return Response(status=400, data='Ни одно оборудование не прошло валидацию')
        return Response(status=201, data=f'Часть оборудования прошла валидацию. Оборудование, не прошедшее валидацию {not_valid}')