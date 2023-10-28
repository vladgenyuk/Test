from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from apps.accounts.models import UserAccount


def v1(request):
    return HttpResponse("Hello from v1")
