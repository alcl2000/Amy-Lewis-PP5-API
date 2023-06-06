from rest_framework import serializers
from projects.models import Projects
from profiles.serializer import ProfileSerializer
from tasks.models import Tasks


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    tasks = serializers.SerializerMethodField()
    # members = ProfileSerializer(read_only=False, many=True)
    # is_member = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        tasks = Tasks.objects.filter(project=obj.id)
        return tasks

    def get_owner_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    # def get_is_member(self, obj):
    #     request = self.context['request']
    #     return request.user in obj.members
    
    class Meta:
        model = Projects
        fields = [
            'id', 'owner', 'owner_id', 'is_owner', 'title', 'goal_1', 'goal_2',
            'goal_3', 'deadline', 'created_on', 'color', 'tasks'
            ]