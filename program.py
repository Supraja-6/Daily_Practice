class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.number = vehicle_number
        self.type = vehicle_type

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

class ParkingLot:
    def __init__(self):
        self.__slots = {
            "Car": 2,
            "Bike": 2,
            "Truck": 1
        }

    def park_vehicle(self, vehicle):
        if self.__slots[vehicle.type] > 0:
            self.__slots[vehicle.type] -= 1
            print(vehicle.type, "parked successfully")
            print("Ticket generated for", vehicle.number)
        else:
            print("No slot available for", vehicle.type)

    def exit_vehicle(self, vehicle, hours):
        fee = self.calculate_fee(vehicle.type, hours)
        self.__slots[vehicle.type] += 1
        print(vehicle.type, "exited")
        print("Parking Fee:", fee)

    def calculate_fee(self, vehicle_type, hours):
        if vehicle_type == "Bike":
            return hours * 20
        elif vehicle_type == "Car":
            return hours * 40
        else:
            return hours * 60

parking = ParkingLot()

car = Car("AP09AB1234", "Car")
bike = Bike("AP09XY5678", "Bike")
#truck = Truck("AP09CY6789", "Truck")

parking.park_vehicle(car)
parking.park_vehicle(bike)
#parking.park_vehicle(truck)

parking.exit_vehicle(car, 3)
parking.exit_vehicle(bike, 2)
#parking.exit_vehicle(truck, 1)



