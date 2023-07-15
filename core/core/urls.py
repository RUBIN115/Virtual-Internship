from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from adventure import views
from django.conf.urls.static import static

from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

# Api routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'coords', views.CoordinatesViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'levels', views.LevelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [    
    path('admin/', admin.site.urls),    
    path('api1/', include(router.urls)),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi/', get_schema_view(
        title="Pass",
        description="Pass application API",
        version="0.1",
    ), name='openapi-schema'),
    path('', include('adventure.urls')),
]

