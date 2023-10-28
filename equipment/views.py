from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import EquipmentType, Equipment
from .serializers import EquipmentTypeSerializer, EquipmentSerializer


class EquipmentTypeListAPIView(ListAPIView):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

