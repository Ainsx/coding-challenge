# Django REST Framework(DRF)
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo  # tells drf to base this serializer on my model
        fields = "__all__"  # id, title, status, created_at
