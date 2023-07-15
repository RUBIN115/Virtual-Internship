from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from adventure import views

from django.conf import settings
from django.conf.urls.static import static

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api2/submit-data/', views.SubmitDataViewSet.as_view(), name='list_or_create_pereval'),
    path('api2/submit-data/<int:pk>/', views.PerevalUpdateView.as_view(), name='read_update_pereval'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)