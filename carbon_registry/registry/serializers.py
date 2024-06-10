from rest_framework import serializers
from .models import Project, CarbonCredit

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class CarbonCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCredit
        fields = '__all__'
