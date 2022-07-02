# from dataclasses import fields
# from django import model
from rest_framework import serializers

from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
