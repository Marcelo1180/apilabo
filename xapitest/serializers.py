from django.contrib.auth.models import User, Group
from models import Archivos
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class ArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos