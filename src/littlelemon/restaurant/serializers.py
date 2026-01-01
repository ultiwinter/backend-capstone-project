# step 5 Set up the menu API - Step 3 create serializers.py in restaurant app
from rest_framework.serializers import ModelSerializer
from rest_framework import generics
from .models import Menu, Booking
from django.contrib.auth.models import User


# step 5 Set up the menu API - Step 4 create serializers for Menu and Booking models
class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


# step 5 Set up the menu API - Step 6 create serializers for User 
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


# step 6 Set up table booking API - Step 2 create serializer for Booking model
class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


