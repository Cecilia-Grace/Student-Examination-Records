from django.shortcuts import render
from .models import Student, Unit
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, UnitSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    permission_classes = [permissions.IsAdminUser]
    
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
    permission_classes = [permissions.IsAdminUser]

    
