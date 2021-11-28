from project.train.train import Train

from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Test", 10)

    def test_initializing_all_attributes(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test_add_passenger_when_train_full_raises(self):
        self.train.capacity = 0
        with self.assertRaises(ValueError) as ex:
            self.train.add("TestPassenger")

        self.assertListEqual([], self.train.passengers)
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_exist_passenger_raises(self):
        self.train.add("TestPassenger")

        with self.assertRaises(ValueError) as ex:
            self.train.add("TestPassenger")

        self.assertListEqual(["TestPassenger"], self.train.passengers)
        self.assertEqual("Passenger TestPassenger Exists", str(ex.exception))

    def test_add_passenger(self):
        self.assertListEqual([], self.train.passengers)
        self.train.add("TestPassenger")
        self.assertListEqual(["TestPassenger"], self.train.passengers)

    def test_remove_not_exist_passenger_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("TestPassenger")

        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_passenger(self):
        self.train.add("TestPassenger")
        self.assertListEqual(["TestPassenger"], self.train.passengers)
        self.train.remove("TestPassenger")
        self.assertListEqual([], self.train.passengers)

if __name__ == "__main__":
    main()