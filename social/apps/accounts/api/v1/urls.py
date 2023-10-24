from django.urls import path, re_path, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from .views import v1, UserApiView

router = DefaultRouter()


urlpatterns = [
    path('', v1, name='v1'),
    path('user/test', UserApiView.as_view(), name='test')
]

urlpatterns += router.urls
