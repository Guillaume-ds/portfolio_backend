from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import *
from . serializers import *


class ExperiencesList(ListAPIView):
    def get(self,request):
        queryset = Experience.objects.all().order_by('-date_deb')
        serializer = ExperienceSerializer(queryset,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
