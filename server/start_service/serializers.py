from rest_framework import serializers

from .models import InformationOverdue


class ModelListSerialializer(serializers.ModelSerializer):

    class Meta:
        model = InformationOverdue
        fields = '__all__'