from rest_framework import serializers
from .models import Tarea

class TareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id','titulo', 'descripcion','completada','fecha_creacion','fecha_limite','prioridad','categoria')
        #no se puede actulizar ni modificar
        read_only_fields= ('fecha_creacion',)
