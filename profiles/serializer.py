from rest_framework import serializers
from .models import Profile
from projects.models import Projects


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Profile picture size larger than 2mb')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_projects(self, obj):
        return Projects.objects.filter(owner=obj.owner.id)

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'created_on', 'name', 'bio',
            'profile_pic', 'projects'
        ]
