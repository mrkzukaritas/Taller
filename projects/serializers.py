from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'description','technologies','created_at','updated_at')
        #no se puede actulizar ni modificar
        read_only_fields= ('created_at',)
