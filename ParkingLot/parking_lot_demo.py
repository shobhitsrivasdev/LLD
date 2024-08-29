from parking_lot import ParkingLot
from level import Level
from car import Car
from bike import Bike
from truck import Truck

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 4))
        parking_lot.add_level(Level(2, 5))

        car = Car("ABC123")
        truck = Truck("XYZ789")
        bike = Bike("M1234")

        # Park vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(bike)

        # Display availability
        parking_lot.display_availability()

        # Unpark vehicle
        parking_lot.unpark_vehicle(bike)

        # Display updated availability
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()