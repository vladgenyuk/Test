
from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework.serializers import ModelSerializer

from apps.accounts.models import UserAccount
from apps.accounts.api.v1.serializers import UserSerializer
from apps.blog.models import Publication


class PublicationSerializer(ModelSerializer):
    publisher = UserSerializer()

    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'publisher']

    def create(self, validated_data):
        user = get_object_or_404(UserAccount, email=validated_data.get('publisher').get('email'))
        publication = Publication.objects.create(
            title=validated_data.get('title'),
            content=validated_data.get('content'),
            published_at=timezone.now(),
            publisher=user
        )
        publication.save()
        return publication
