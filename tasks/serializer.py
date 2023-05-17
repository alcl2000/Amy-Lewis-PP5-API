from tasks.models import Tasks
from rest_framework import serializers


class TaskSerializer(serializers.ModelField):
    user = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_owner_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Tasks
        fields = [
            'id', 'user', 'is_owner', 'title', 'progress',
            'due_date', 'created_on', 'important'
        ]