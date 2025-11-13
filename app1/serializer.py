from rest_framework import serializers
from .models import trainer
class trainerserializer(serializers.ModelSerializer):
    class meta:
        model=trainer
        fields='__all__'
