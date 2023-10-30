from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('equipment.urls')),
    path('api/user/login/', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
]

urlpatterns += doc_urls
