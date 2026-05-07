from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members_detail = UserSerializer(source='members', many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'owner', 'members', 'members_detail', 'created_at')
        read_only_fields = ('id', 'created_at')
