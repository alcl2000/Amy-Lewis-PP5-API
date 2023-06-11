from rest_framework import serializers
from projects.models import Projects
from profiles.serializer import ProfileSerializer
from profiles.models import Profile
from tasks.models import Tasks
from tasks.serializer import TaskSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    # owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_id = serializers.SerializerMethodField()
    tasks = TaskSerializer(read_only=False, many=True, required=False)
    members = ProfileSerializer(read_only=False, many=True, required=False)
    is_member = serializers.SerializerMethodField()

    def get_owner_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner_id

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_is_member(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            member = Profile.objects.filter(projects=obj.id,
                                            owner=request.user.id)
            return True
        return False

    class Meta:
        model = Projects
        fields = [
            'id', 'owner_name', 'owner_id', 'is_owner', 'title', 'goal_1',
            'goal_2', 'goal_3', 'deadline', 'created_on', 'color', 'tasks',
            'members', 'is_member'
            ]
