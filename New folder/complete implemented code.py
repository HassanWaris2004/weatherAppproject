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

# Example usage
if __name__ == "__main__":
    my_car = Car()
    my_bike = Bike()
    
    service = VehicleService()
    
    # Interacting with Car
    print("Interacting with Car:")
    service.start_vehicle(my_car)
    service.stop_vehicle(my_car)
    
    print("\nInteracting with Bike:")
    # Interacting with Bike
    service.start_vehicle(my_bike)
    service.stop_vehicle(my_bike)
