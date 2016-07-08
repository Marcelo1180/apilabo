#!/usr/bin/python
# -*- coding: utf8 -*-
from django.shortcuts import render
from serializers import ArchivosSerializer
from rest_framework import viewsets
from models import Archivos
# from models import User, Group
from django.contrib.auth.models import User, Group


class ArchivosViewSet(viewsets.ModelViewSet):
    """
    ## Api de Prueba
    """
    queryset = Archivos.objects.all()
    serializer_class = ArchivosSerializer


# ----------------------------------------------------------------------------------------------
# JWToken DATA
# ----------------------------------------------------------------------------------------------
from serializers import UserSerializer
import json


def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'user': UserSerializer(user).data,
        'menu': json.loads(Group.objects.get(name="SUPERUSER").menu) if user.is_superuser else json.loads(user.groups.all()[0].menu),
    }