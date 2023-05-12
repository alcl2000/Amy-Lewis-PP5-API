from rest_framework import serializers
from projects.models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source=owner.username)
    # is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source=owner.id)
    tasks = serializers.ReadOnlyField()
    
    class Meta:
        model = Projects
        fields = [
            'id', 'owner', 
        ]