from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, CarbonCredit
from .serializers import ProjectSerializer, CarbonCreditSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CarbonCreditViewSet(viewsets.ModelViewSet):
    queryset = CarbonCredit.objects.all()
    serializer_class = CarbonCreditSerializer

def index(request):
    return render(request, 'index.html')
# Create your views here.
