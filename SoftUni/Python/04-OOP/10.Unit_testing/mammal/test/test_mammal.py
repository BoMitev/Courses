from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Bear", "roar")

    def test_initialization_all_attributes(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Bear", self.mammal.type)
        self.assertEqual("roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        self.assertEqual(f"Test makes roar", self.mammal.make_sound())

    def test_get_kingdom_getter(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_mammal_info(self):
        self.assertEqual(f"Test is of type Bear", self.mammal.info())


if __name__ == "__main__":
    main()