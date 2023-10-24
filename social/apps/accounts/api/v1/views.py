from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from apps.accounts.models import UserAccount


def v1(request):
    return HttpResponse("Hello from v1")


class UserApiView(APIView):
    permission_classes = []

    def get(self, request, format=None):
        print(UserAccount.objects.get(email='vladgenyuk29@gmail.com'))
        return Response(None)