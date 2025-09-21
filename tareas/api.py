from .models import Tarea
from .serializers import TareSerializer
from rest_framework import viewsets , permissions
class TareaViewSet(viewsets.ModelViewSet):
    queryset=Tarea.objects.all()
    #i sauntentica si esta autenticado 
    permission_classes= [permissions.AllowAny]
    serializer_class = TareSerializer