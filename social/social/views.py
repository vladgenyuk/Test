from django.shortcuts import render
from django.http import HttpResponseNotFound


def handler404(request, exception):
    return render(request, 'project/error_404.html')


