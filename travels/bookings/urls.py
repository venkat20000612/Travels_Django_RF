
from django.urls import path
from.views import register_view, Login_view, BusListCreateView, UserBookingView, BookingView

urlpatterns = [
  path('buses/', BusListCreateView.as_view(), name= 'buslist'),
  path('regiter/', register_view.as_view(), name='register'),
  path('login/', Login_view.as_view(), name='login'),
  path('user/<int:user_id>/bookings/', UserBookingView.as_view(), name='user-bookings'),
  path('booking/', BookingView.as_view(), name='booking')
]