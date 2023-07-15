from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response
import django_filters
from .filters import PerevalFilter
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CoordinatesViewSet(viewsets.ModelViewSet):
    """
    Pass Coordinates view API endpoint
    """
    queryset = Coordinate.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = [permissions.AllowAny]


class ImageViewSet(viewsets.ModelViewSet):
    """
    Pass images view API endpoint
    """
    queryset = Image.objects.all().order_by('-date_added')
    serializer_class = ImagesSerializer
    permission_classes = [permissions.AllowAny]


class LevelViewSet(viewsets.ModelViewSet):
    """
    Level images view API endpoint
    """
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.AllowAny]

class PerevalListView(ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_class = PerevalFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class PerevalListView(ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_class = PerevalFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class SubmitDataViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["user__email"]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class PerevalUpdateView(RetrieveUpdateAPIView):

    queryset = Pereval.objects.all()
    serializer_class = PerevalUpdateSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Status not New')
            serializer.save()
            return Response({'state': 1, 'message': 'Update successfully'})
        else:
            return Response({'state': 0, 'message': serializer.errors})
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Status not New')
            serializer.save()
            return Response({'state': 1, 'message': 'Update successfully'})
        else:
            return Response({'state': 0, 'message': serializer.errors})