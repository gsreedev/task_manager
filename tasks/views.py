from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer
from .permissions import TaskPermission
from django.db.models import Q

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, TaskPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Admin':
            return Task.objects.all()
        # Members can see tasks in projects they are a part of
        return Task.objects.filter(Q(project__members=user) | Q(assignee=user)).distinct()
    
    def perform_update(self, serializer):
        user = self.request.user
        if user.role == 'Member':
            # Members can only update the status
            serializer.save(status=serializer.validated_data.get('status', serializer.instance.status),
                            title=serializer.instance.title,
                            description=serializer.instance.description,
                            project=serializer.instance.project,
                            assignee=serializer.instance.assignee,
                            due_date=serializer.instance.due_date)
        else:
            serializer.save()

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        user = request.user
        if user.role == 'Admin':
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(assignee=user)

        total = tasks.count()
        pending = tasks.filter(status='Pending').count()
        in_progress = tasks.filter(status='In Progress').count()
        completed = tasks.filter(status='Completed').count()
        
        today = timezone.now().date()
        overdue = tasks.filter(due_date__lt=today).exclude(status='Completed').count()

        return Response({
            'total': total,
            'pending': pending,
            'in_progress': in_progress,
            'completed': completed,
            'overdue': overdue
        })
