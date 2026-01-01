from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Step 2 Django Static Routes - Step 4 define index view
def index(request):
    context = {
            "current_year": now().year
        }
    return render(request, 'index1.html', context)


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

# step 6 Set up table booking API - Step 3 create Booking API views
# difference between ModelViewSet and ListCreateAPIView + RetrieveUpdateDestroyAPIView is that
# ModelViewSet combines all CRUD operations into a single class
# ListCreateAPIView handles listing and creating resources
# RetrieveUpdateDestroyAPIView handles retrieving, updating, and deleting resources
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# step 6 set up table booking API - Step 5 create User API view
class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 


# additional views
def about_page(request):
    context = {"current_year": now().year}
    return render(request, "about.html", context)


def menu_page(request):
    menu_items = Menu.objects.all()
    context = {
        "menu_items": menu_items,
        "current_year": now().year
    }
    return render(request, "menu.html", context)


def booking_page(request):
    context = {"current_year": now().year}
    return render(request, "booking.html", context)

