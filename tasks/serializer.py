from tasks.models import Tasks
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Tasks
        fields = [
            'id', 'user', 'is_owner', 'title', 'progress',
            'due_date', 'created_on', 'important'
        ]