from rest_framework import serializers
from .models import Classroom, DoubtSection
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings


class ClassroomSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Classroom
        fields =('__all__')
        #fields = ('class_code','subject_name','subject_code','description','standard','branch','section')

class DoubtSectionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = DoubtSection
        fields =('__all__')