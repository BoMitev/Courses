from project.factory.paint_factory import PaintFactory

from unittest import TestCase, main


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Test", 100)

    def test_initializing_all_attributes(self):
        self.assertEqual("Test", self.paint_factory.name)
        self.assertEqual(100, self.paint_factory.capacity)
        self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertDictEqual(self.paint_factory.products, self.paint_factory.ingredients)

    def test_can_add(self):
        self.paint_factory.ingredients = {"white": 10, "yellow": 10}
        result = self.paint_factory.can_add(50)
        self.assertEqual(True, result)

        result2 = self.paint_factory.can_add(90)
        self.assertEqual(False, result2)

    def test_add_gradient_invalid_product_type_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("pink", 10)

        self.assertEqual("Ingredient of type pink not allowed in PaintFactory", str(ex.exception))

    def test_add_gradient_not_enough_space_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 120)

        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_gradient_successfully(self):
        self.assertDictEqual({}, self.paint_factory.products)
        result = self.paint_factory.add_ingredient("white", 50)
        self.assertDictEqual({"white": 50}, self.paint_factory.products)
        self.assertIsNone(result)

        self.paint_factory.add_ingredient("white", 10)
        self.assertDictEqual({"white": 60}, self.paint_factory.products)

        self.paint_factory.add_ingredient("yellow", 10)
        self.assertDictEqual({"white": 60, "yellow": 10}, self.paint_factory.products)

    def test_remove_gradient_not_found_rises(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("white", 10)

        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_gradient_less_than_zero(self):
        self.paint_factory.ingredients = {"white": 10}
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 20)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_gradient_successfully(self):
        self.paint_factory.ingredients = {"white": 20}
        result = self.paint_factory.remove_ingredient("white", 10)
        self.assertDictEqual({"white": 10}, self.paint_factory.ingredients)
        self.assertIsNone(result)

    def test_repr_representation(self):
        self.paint_factory.ingredients = {"white": 10, "yellow": 10}
        expected = "Factory name: Test with capacity 100.\n" \
                   "white: 10\n" \
                   "yellow: 10\n"
        self.assertEqual(expected, repr(self.paint_factory))


if __name__ == "__main__":
    main()