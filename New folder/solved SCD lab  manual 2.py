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
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")

    def stop_engine(self):
        print("Motorcycle engine stopped.")

        my_car = Car()
my_car.start_engine()
my_car.stop_engine()

my_motorcycle = Motorcycle()
my_motorcycle.start_engine()
my_motorcycle.stop_engine()

