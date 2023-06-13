from tasks.models import Tasks
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Tasks
        fields = [
            'id', 'owner', 'is_owner', 'title', 'progress',
            'due_date', 'created_on', 'important', 'project'
        ]
