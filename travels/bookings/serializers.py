from rest_framework import serializers
from.models import Bus, Seat, Booking
from django.contrib.auth.models import User


class User_register_serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )
        return user


class Bus_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class Seat_serializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'is_booked']


class Booking_serilaizer(serializers.ModelSerializer):
    bus = serializers.StringRelatedField()
    seat = serializers
    user = serializers.StringRelatedField()
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'booking_time', 'bus', 'seat']