from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This is for the bus details in the database
class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    features = models.TextField()
    start_time = models.TimeField()
    reach_time = models.TimeField()
    no_of_seats = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    # This line is showing the bus names , number, etc what we have define here
    def __str__(self):
        return f"{self.bus_name} {self.bus_number} {self.origin} {self.destination}"
    
    
    



# this is the that bus seats availabity in data base
class Seat(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

     # This line is showing the bus names , seat number, etc what we have define here
    def __str__(self):
        return f"{self.bus} {self.seat_number} {self.is_booked}"
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.bus.bus_name} {self.bus.start_time} {self.bus.reach_time} {self.seat.seat_number}"
