from project.pet_shop import PetShop

from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.petshop = PetShop("Test")

    def test_initializing_all_attributes(self):
        self.assertEqual("Test", self.petshop.name)
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test_add_food_negative_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.petshop.add_food("TestFood", 0)

        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food(self):
        self.petshop.add_food("TestFood", 10)
        self.assertDictEqual({"TestFood": 10}, self.petshop.food)

        result = self.petshop.add_food("TestFood", 10)
        self.assertDictEqual({"TestFood": 20}, self.petshop.food)
        self.assertEqual("Successfully added 10.00 grams of TestFood.", result)

    def test_add_existing_pet_raises(self):
        self.petshop.add_pet("TestPet")
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet("TestPet")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet(self):
        self.assertListEqual([], self.petshop.pets)
        result = self.petshop.add_pet("TestPet")
        self.assertListEqual(["TestPet"], self.petshop.pets)
        self.assertEqual("Successfully added TestPet.", result)

    def test_feed_not_existing_pet_raises(self):
        self.petshop.add_pet("TestPet")
        self.petshop.add_food("TestFood", 10)

        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet("TestFood", "PetTest")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_not_exist(self):
        self.petshop.add_pet("TestPet")
        self.petshop.add_food("TestFood", 10)

        result = self.petshop.feed_pet("FoodTest", "TestPet")
        self.assertEqual("You do not have FoodTest", result)

    def test_feed_pet_with_less_than_hundred(self):
        self.petshop.add_pet("TestPet")
        self.petshop.add_food("TestFood", 10)
        self.assertDictEqual({"TestFood": 10}, self.petshop.food)

        result = self.petshop.feed_pet("TestFood", "TestPet")
        self.assertDictEqual({"TestFood": 1010}, self.petshop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet(self):
        self.petshop.add_pet("TestPet")
        self.petshop.add_food("TestFood", 100)
        self.assertDictEqual({"TestFood": 100}, self.petshop.food)

        result = self.petshop.feed_pet("TestFood", "TestPet")
        self.assertDictEqual({"TestFood": 0}, self.petshop.food)
        self.assertEqual("TestPet was successfully fed", result)

    def test_repr_representation(self):
        self.petshop.add_pet("TestPet")
        self.petshop.add_pet("TestPet2")

        self.assertEqual(f'Shop Test:\n'
                         f'Pets: TestPet, TestPet2', repr(self.petshop))


if __name__ == "__main__":
    main()