from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'content', 'created_on','code_url','picture',"tags","language"]