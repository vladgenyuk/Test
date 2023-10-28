from django.shortcuts import render


def oauth(request):
    return render(request, 'oauth/index.html')
