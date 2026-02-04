from .views import StudentViewSet, UnitViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r'Student', StudentViewSet, basename='Students')
router.register(r'Unit', UnitViewSet, basename='Units')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
