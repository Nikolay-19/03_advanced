import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def test_init_no_courses(self):
        a = Student("B")
        self.assertEqual("B", a.name)
        self.assertEqual({}, a.courses)

    def test_init_with_courses_no_notes(self):
        a = Student("B", {"C": []})
        self.assertEqual("B", a.name)
        self.assertEqual({"C": []}, a.courses)

    def test_init_with_courses_with_notes(self):
        a = Student("B", {"C": [1, 2, 3]})
        self.assertEqual("B", a.name)
        self.assertEqual({"C": [1, 2, 3]}, a.courses)

    def test_add_new_no_notes(self):
        a = Student("B")
        self.assertEqual("Course has been added.", a.enroll("C", "", "N"))
        self.assertEqual({"C": []}, a.courses)

    def test_add_new_with_notes(self):
        a = Student("B")
        self.assertEqual("Course and course notes have been added.", a.enroll("C", ["A"], ""))
        self.assertEqual({"C": ["A"]}, a.courses)

    def test_add_new_with_notes_y(self):
        a = Student("B")
        self.assertEqual("Course and course notes have been added.", a.enroll("C", ["A"], "Y"))
        self.assertEqual({"C": ["A"]}, a.courses)

    def test_add_existing_course(self):
        a = Student("B", {"C": []})
        self.assertEqual("Course already added. Notes have been updated.", a.enroll("C", "A", "N"))
        self.assertEqual({"C": ["A"]}, a.courses)

    def test_add_notes_existing_course(self):
        a = Student("B", {"C": []})
        self.assertEqual("Notes have been updated", a.add_notes("C", [1, 2, 3]))
        self.assertEqual({"C": [[1, 2, 3]]}, a.courses)

    def test_add_notes_non_existing_course(self):
        a = Student("B")
        with self.assertRaises(Exception) as ex:
            a.add_notes("C", [1, 2, 3])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception.args[0]))

    def test_leave_existing_course(self):
        a = Student("B", {"C": []})
        self.assertEqual("Course has been removed", a.leave_course("C"))
        self.assertEqual({}, a.courses)

    def test_leave_non_existing_course(self):
        a = Student("B")
        with self.assertRaises(Exception) as ex:
            a.leave_course("C")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception.args[0]))


if __name__ == "__main__":
    unittest.main()
