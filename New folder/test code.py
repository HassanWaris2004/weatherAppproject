from abc import ABC, abstractmethod

# Define the Vehicle interface
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Implement the Car class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a smooth roar.")

    def stop_engine(self):
        print("Car engine stopped with a gentle hum.")

# Implement the Bike class
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with a powerful vroom!")

    def stop_engine(self):
        print("Bike engine stopped quickly.")

# Create the VehicleService class
class VehicleService:
    def start_vehicle(self, vehicle: Vehicle):
        vehicle.start_engine()

    def stop_vehicle(self, vehicle: Vehicle):
        vehicle.stop_engine()

# Test program
if __name__ == "__main__":
    # Create instances of Car and Bike
    my_car = Car()
    my_bike = Bike()
    
    # Create an instance of VehicleService
    service = VehicleService()
    
    # Test the VehicleService with Car
    print("Testing VehicleService with Car:")
    service.start_vehicle(my_car)
    service.stop_vehicle(my_car)
    
    print("\nTesting VehicleService with Bike:")
    # Test the VehicleService with Bike
    service.start_vehicle(my_bike)
    service.stop_vehicle(my_bike)
