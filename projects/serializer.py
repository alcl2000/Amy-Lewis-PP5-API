from rest_framework import serializers
from projects.models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source=owner.username)
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source=owner.id)
    tasks = serializers.ReadOnlyField()

    def get_owner_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Projects
        fields = [
            'id', 'owner', 'is_owner', 'due_date', 'created_at',
            'assigned_users', 'completed_tasks', 'goal_1', 'goal_2',
            'goal_3', 'colors', 'tasks'
            ]