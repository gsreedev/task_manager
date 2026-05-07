from rest_framework import serializers
from .models import Task
from projects.serializers import ProjectSerializer
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    project_detail = ProjectSerializer(source='project', read_only=True)
    assignee_detail = UserSerializer(source='assignee', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'project', 'project_detail', 'assignee', 'assignee_detail', 'status', 'due_date', 'created_at')
        read_only_fields = ('id', 'created_at')
