from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Test", {"course": ["note", "note1"]})

    def test_initializing_all_attributes(self):
        self.assertEqual("Test", self.student.name)
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)

        student = Student("Testov")
        self.assertEqual("Testov", student.name)
        self.assertDictEqual({}, student.courses)

    def test_add_notes_if_course_exist(self):
        result = self.student.enroll("course", ["note2", "note3"])
        self.assertDictEqual({"course": ["note", "note1", "note2", "note3"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_and_course(self):
        result = self.student.enroll("course2", ["note2"])
        self.assertDictEqual({"course": ["note", "note1"], "course2": ["note2"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

        result2 = self.student.enroll("course3", ["note3"], "Y")
        self.assertDictEqual({"course": ["note", "note1"], "course2": ["note2"], "course3": ["note3"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result2)

    def test_add_course(self):
        result = self.student.enroll("course2", ["note1"], "N")

        self.assertDictEqual({"course": ["note", "note1"], "course2": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_successfully(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        result = self.student.add_notes("course", "note2")
        self.assertDictEqual({"course": ["note", "note1", "note2"]}, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_course_not_found_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("course1", "note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_successfully(self):
        self.assertDictEqual({"course": ["note", "note1"]}, self.student.courses)
        result = self.student.leave_course("course")
        self.assertDictEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_unknown_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("course1")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()