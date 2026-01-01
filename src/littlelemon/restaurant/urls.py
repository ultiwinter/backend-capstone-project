from django.contrib import admin 
from django.urls import path 
from .views import index, MenuItemsView, SingleMenuItemView, menu_page, booking_page, about_page
from rest_framework.authtoken.views import obtain_auth_token # step 8 Securing the table booking API - Step 4 import obtain_auth_token
  
urlpatterns = [ 
    path('', index, name='home'), # Step 2 Django Static Routes - Step 5 Add URL Route for index view
    path('menu/', MenuItemsView.as_view()), # step 5 Set up the menu API - Step 5 add URL patterns for Menu API
    path('menu/<int:pk>', SingleMenuItemView.as_view()), # step 5 Set up the menu API - Step 5 add URL patterns for Menu API
    # path('booking/', include(router.urls)),
    
    # additional stuff
    path("menu-page/", menu_page, name="menu"),
    path("booking-page/", booking_page, name="booking"),
    path("about/", about_page, name="about"),
]