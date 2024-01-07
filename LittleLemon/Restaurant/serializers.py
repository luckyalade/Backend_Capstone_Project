from rest_framework import serializers
from .models import Menu, Booking

# Define a serializer for the Menu model
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# Define a serializer for the Booking model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
