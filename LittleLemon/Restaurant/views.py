from django.shortcuts import render
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Define the index view
def index(request):
  return render(request, 'index.html', {})

# Define the menu item view
class MenuItemView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]

  # Define the index view for the menu items
  def index(request):
    print(request.user)
    return render(request, 'index.html', {})


# Define the single menu item view
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]

# Define the booking view set
class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]
