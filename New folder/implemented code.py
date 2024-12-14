from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a smooth roar.")

    def stop_engine(self):
        print("Car engine stopped with a gentle hum.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with a powerful vroom!")

    def stop_engine(self):
        print("Bike engine stopped quickly.")

# Example usage
my_car = Car()
my_car.start_engine()
my_car.stop_engine()

my_bike = Bike()
my_bike.start_engine()
my_bike.stop_engine()

def test_vehicle(vehicle: Vehicle):
    vehicle.start_engine()
    vehicle.stop_engine()

# Testing with different vehicle types
test_vehicle(my_car)
test_vehicle(my_bike)
