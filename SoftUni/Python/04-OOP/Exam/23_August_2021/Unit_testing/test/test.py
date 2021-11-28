from project.library import Library

from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Test")

    def test_initializing_all_attributes(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

        with self.assertRaises(ValueError) as ex:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        self.assertDictEqual({}, self.library.books_by_authors)
        self.library.add_book("Ivan", "TestTitle")
        self.assertDictEqual({"Ivan": ["TestTitle"]}, self.library.books_by_authors)

        self.library.add_book("Ivan", "TestTitle2")
        self.assertDictEqual({"Ivan": ["TestTitle", "TestTitle2"]}, self.library.books_by_authors)

    def test_add_reader(self):
        self.assertDictEqual({}, self.library.readers)
        self.library.add_reader("Ivan")
        self.assertDictEqual({"Ivan": []}, self.library.readers)

        result = self.library.add_reader("Ivan")
        self.assertEqual("Ivan is already registered in the Test library.", result)

    def test_rent_book_reader_not_exist(self):
        self.library.add_book("Ivan", "TestTitle")
        result = self.library.rent_book("TestReader", "Ivan", "TestTitle")

        self.assertEqual("TestReader is not registered in the Test Library.", result)

    def test_rent_book_author_not_exist(self):
        self.library.add_reader("TestReader")
        result = self.library.rent_book("TestReader", "Ivan", "TestTitle")

        self.assertEqual("Test Library does not have any Ivan's books.", result)

    def test_rent_book_title_not_exist(self):
        self.library.add_book("Ivan", "TestTitle")
        self.library.add_reader("TestReader")
        result = self.library.rent_book("TestReader", "Ivan", "TitleNotExist")

        self.assertEqual(f"""Test Library does not have Ivan's "TitleNotExist".""", result)

    def test_rent_book(self):
        self.library.add_book("Ivan", "TestTitle")
        self.library.add_reader("TestReader")
        self.library.rent_book("TestReader", "Ivan", "TestTitle")

        self.assertDictEqual({"TestReader": [{"Ivan": "TestTitle"}]}, self.library.readers)
        self.assertDictEqual({"Ivan": []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()