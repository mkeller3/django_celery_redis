from rest_framework import serializers
from .models import *

class taskSerializer(serializers.Serializer):
    task_id = serializers.CharField()