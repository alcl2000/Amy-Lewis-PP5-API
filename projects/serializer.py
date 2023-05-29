from rest_framework import serializers
from projects.models import Projects
from profiles.serializer import ProfileSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    tasks = serializers.ReadOnlyField()
    members = ProfileSerializer(many=True)
    is_member = serializers.SerializerMethodField()

    def get_owner_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner 
    
    def get_is_member(self, obj):
        request = self.context['request']
        return request.user in obj.members
    
    class Meta:
        model = Projects
        fields = [
            'id', 'owner', 'is_owner', 'title', 'goal_1', 'goal_2', 'goal_3' 
            'deadline', 'created_at', 'assigned_users', 'completed_tasks',
            'color', 'tasks', 'members', 'is_member'
            ]