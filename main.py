from database import create_table
from car import Car
from motocycle import Motorcycle
from fleet_manager import FleetManager


def main():
    create_table()
    manager = FleetManager()

    car1 = Car('Toyota', 'Camry', 2018, 5)
    bike1 = Motorcycle('Honda', 'CB750', 2014, False)

    manager.add_vehicle(car1)
    manager.add_vehicle(bike1)

    manager.list_vehicles()
    manager.find_vehicle("Toyota")
    manager.update_vehicle("Toyota", "Corolla")

    manager.list_vehicles()

    manager.remove_vehicle("Harley")

    manager.list_vehicles()

    manager.close()


main()