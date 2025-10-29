class Vehicle:
    def __init__(self,_vehicle_id,_base_rate):
        self._vehicle_id = _vehicle_id
        self._base_rate = _base_rate
    def display_details(self):
        return f"vehicle_id: {self._vehicle_id} base_rate:₹{self._base_rate:.2f}"
    def rental_charge(self):
        return 0.0
    
class Car(Vehicle):
    def __init__(self,_vehicle_id,_base_rate,num_seats):
        super().__init__(_vehicle_id,_base_rate)
        self.num_seats = num_seats
    def  rental_charge(self):
        return self._base_rate * self.num_seats

class Bike(Vehicle):
    def __init__(self, _vehicle_id, _base_rate,bike_type):
        super().__init__(_vehicle_id, _base_rate)
        self.bike_type = bike_type
    def rental_charge(self):
        return self._base_rate * 0.5
Car1 = Car("CAR001" , 100.00, 4)
print(Car1.display_details())
print("Car Rental Charge per day: ₹",Car1.rental_charge())

Bike1 = Bike("BIKE001",500.0,"Scooter")
print(Bike1.display_details())
print("Car Rental Charge per day: ₹",Bike1.rental_charge())

# You are tasked with building a Vehicle Rental Management System to help a car rental company manage different types of vehicles (Cars and Bikes) and calculate their rental charges for billing purposes. 
# Requirements:

# Create a base class Vehicle to store common vehicle details.
# Attributes (protected, not private):
#      _vehicle_id: A string representing the unique vehicle identifier (e.g., "CAR001", "BIKE001").
#      _base_rate: A float representing the base daily rental rate (e.g., 100.00).
# Include a constructor to initialize _vehicle_id and _base_rate.
# Provide a method display_details() to return a string with the vehicle ID and base rate.
# Include a method rental_charge() that returns a placeholder value (0.0) to be overridden by subclasses.x

# Create a subclass Car that inherits from Vehicle:
#      Add an attribute num_seats (integer, e.g., 4 for a sedan).
#      Override the rental_charge() method to calculate the daily rental charge as _base_rate * num_seats.
# Create a subclass Bike that inherits from Vehicle:
#      Add an attribute bike_type (string, e.g., "Scooter", "Motorcycle").
#      Override the rental_charge() method to calculate the daily rental charge as _base_rate * 0.5.

# Write a function calculate_rental that accepts a Vehicle object and calls its rental_charge() method to return the rental charge. This demonstrates polymorphism by working with any vehicle type.
    
       