class Vehicle:
    def drive(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Car(Vehicle):
    def drive(self):
        return "Driving a car."

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike."

class Truck(Vehicle):
    def drive(self):
        return "Driving a truck."
b
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# Example usage
if __name__ == "__main__":
    vehicle_type = input("Enter vehicle type (car/bike/truck): ").lower()
    try:
        vehicle = VehicleFactory.create_vehicle(vehicle_type)
        print(vehicle.drive())
    except ValueError as e:
        print(e)
