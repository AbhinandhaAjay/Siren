# accidents/serializers.py

from rest_framework import serializers
from .models import Accident

class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = '__all__'  # includes new fields: severity_score, status

