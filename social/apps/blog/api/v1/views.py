from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import PublicationSerializer
from apps.blog.models import Publication
from apps.accounts.models import UserAccount


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    permission_classes = []
    serializer_class = PublicationSerializer

    def retrieve(self, request, pk=None):
        publication = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(publication)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'info': 'Publication created',
                             'details': serializer.data}, status=201)
        return Response(serializer.errors)

    # def update(self):
