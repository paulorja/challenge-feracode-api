from rest_framework import serializers
from .models import Diapers


class DiapersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diapers
        fields = ("model", "size")
