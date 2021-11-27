from project.vehicle import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_instance_attr_are_set(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_check_capacity_unchanged_if_fuel_changed(self):
        self.assertEqual(50, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(50, self.vehicle.capacity)

    def test_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_drive_more_than_amount_of_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)

        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.fuel = 20
        self.vehicle.refuel(20)
        self.assertEqual(40, self.vehicle.fuel)

    def test_refuel_overflow_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_representation(self):
        self.assertEqual(f"The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()
