from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet, basename='equipment')

urlpatterns = [
    path('equipment_type/', views.EquipmentTypeListAPIView.as_view(), name='get_equipment_types'),
]

urlpatterns += router.urls