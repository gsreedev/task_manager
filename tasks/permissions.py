from rest_framework import permissions

class TaskPermission(permissions.BasePermission):
    """
    Custom permission for tasks:
    - Admin can do anything.
    - Members can only update status of their assigned tasks.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Admin':
            return True
        
        # If member, they can only view or update status if they are the assignee
        if obj.assignee == request.user:
            if request.method in permissions.SAFE_METHODS:
                return True
            # Allow members to change status (PATCH/PUT) but in serializer we might need to restrict other fields
            if request.method in ['PUT', 'PATCH']:
                return True
        return False
