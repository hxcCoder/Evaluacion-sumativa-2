# Evaluacion-sumativa-1/Autos/serializers.py[cite: 2]
from rest_framework import serializers
from .models import Auto

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = "__all__"