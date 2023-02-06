from .models import Project
from rest_framework import viewsets, permissions
# Serializers
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # with this we consult (request) all data of a TABLE
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    # to this point we already have created our API
    