from django.shortcuts import render

# Create your views here.

# authication, premission, token, status, response, generics, apiviews
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from rest_framework.views import APIView
from.serializers import User_register_serializer, Bus_serializer, Booking_serilaizer
from rest_framework.response import Response
from.models import Bus, Seat, Booking

# This is for the register
class register_view(APIView):
    def post(self, request):
        serializer = User_register_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# This is for the login
class Login_view(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username= username, password= password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id
            }, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Inavlid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        


# This is for the bus list
class BusListCreateView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = Bus_serializer


# This is for the bus details view
class BusdetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = Bus_serializer

# This is for the bus seat booking view

class BookingView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        seat_id = request.data.get('seat')
        try:
            seat = Seat.objects.get(id= seat_id)
            if seat.is_booked:
                return Response({'error': 'Seat already booked'}, status=status.HTTP_400_BAD_REQUEST)
            
            seat.is_booked = True
            seat.save()

            bookings = Booking.objects.create(
                user = request.user,
                bus = seat.bus,
                seat = seat
            )

            serializer = Booking_serilaizer(bookings)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        except Seat.DoesNotExist:
            return Response({'error': 'Invalid seat id'}, status=status.HTTP_400_BAD_REQUEST)
        


# This is for user booking details view

class UserBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        if request.user.id != user_id:
                return Response({'error': 'Unautherised'}, status= status.HTTP_401_UNAUTHORIZED)
        
        bookings = Booking.objects.filter(user_id= user_id)
        serializer = Booking_serilaizer(bookings, many= True)
        return Response(serializer.data)
