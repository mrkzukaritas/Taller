from rest_framework import routers
from .api import TareaViewSet

routers= routers.DefaultRouter()

routers.register('api/tareas',TareaViewSet,'Tareas')

urlpatterns= routers.urls