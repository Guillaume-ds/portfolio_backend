from rest_framework import serializers
from .models import *


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ['title', 'date_deb', 'date_fin', 'description1','description2','description3',"lien","queryParams"]