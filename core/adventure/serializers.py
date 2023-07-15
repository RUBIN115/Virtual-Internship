from django.http import Http404
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.validators import UniqueValidator
from .models import *


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    phone = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    middle_name = models.CharField()

    class Meta:
        model = Users
        fields = ['pk', 'phone', 'first_name', 'last_name', 'email', 'middle_name']

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['latitude', 'longitude', 'height',]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'image']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']

    
class PerevalSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    user = UserSerializer()
    coord = CoordinatesSerializer()
    level = LevelSerializer()
    image = ImagesSerializer()

    class Meta:
        model = Pereval
        exclude = ('status', )

    def validate(self, attrs):
        print('validator')
        user_data = attrs.get('user')
        if not user_data:
            raise ValidationError("User data is missing.")

        if self.instance:
            user = self.instance.user            
        else:
            try:
                user = Users.objects.get(email=user_data.get('email')) # .exists())                
            except Users.DoesNotExist:
                user = None      
            
     
        if user is not None:
            if user.first_name != user_data.get('first_name') or \
                    user.last_name != user_data.get('last_name') or user.middle_name != user_data.get('middle_name') or \
                    user.phone != user_data.get('phone') or user.email != user_data.get('email'):
                raise ValidationError("Information cannot be changed")

        super().validate(attrs)

        return attrs
    
    def create(self, validated_data):

        user_data = validated_data.pop('user')   

        coord_data = validated_data.pop('coord')
        coord = Coordinate.objects.create(**coord_data)

        level_data = validated_data.pop('level')
        level = Level.objects.create(**level_data)

        images_data = validated_data.pop('image') 
        image = Image.objects.create(**images_data)

        if Pereval.objects.filter(user__email=user_data.get('email')).exists():     
            user = Users.objects.get(email=user_data.get('email')).pk            
            pereval = Pereval.objects.create(**validated_data, user=Users.objects.get(email=user_data.get('email')), level=level, coord=coord, image=image)   
        else:
            user = Users.objects.create(**user_data)
            pereval = Pereval.objects.create(**validated_data, user=user, level=level, coord=coord, image=image)
        return pereval

class PerevalUpdateSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):

    coord = CoordinatesSerializer()
    level = LevelSerializer()
    image = ImagesSerializer()
    
    class Meta:
        model = Pereval
        fields = '__all__'
        read_only_fields = ['user', ]

