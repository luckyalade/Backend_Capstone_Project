from django.shortcuts import render
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

def index(request):
  return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]

  def index(request):
    print(request.user)
    return render(request, 'index.html', {})



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuItemSerializer
  permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]
