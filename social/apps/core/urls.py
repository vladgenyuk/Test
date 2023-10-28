from django.urls import path, include
from .views import home


urlpatterns = [
    path('home/', home, name='core'),
    path('blog/', include('apps.blog.urls'))
]
