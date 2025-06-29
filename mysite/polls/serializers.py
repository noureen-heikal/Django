from rest_framework import serializers
from .models import YourModelName  # Replace with your actual model

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModelName
        fields = '__all__'