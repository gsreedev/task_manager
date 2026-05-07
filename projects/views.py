from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAdminUserOrReadOnly, IsProjectOwnerOrAdmin
from django.db.models import Q

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly, IsProjectOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Admin':
            return Project.objects.all()
        return Project.objects.filter(Q(owner=user) | Q(members=user)).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
