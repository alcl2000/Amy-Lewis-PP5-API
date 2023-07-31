from tasks.models import Tasks
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Tasks
        fields = [
            'id', 'owner_name', 'owner_id', 'is_owner', 'title', 'progress',
            'due_date', 'created_on', 'important', 'project'
        ]
