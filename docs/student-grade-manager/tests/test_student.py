
import sys
from pathlib import Path
import unittest


PROJECT_FOLDER = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_FOLDER)
)


from student import Student


class TestStudent(unittest.TestCase):

    def test_student_details(self):

        student = Student(
            1001,
            "Ashok",
            [80, 90, 85]
        )

        self.assertEqual(
            student.student_id,
            1001
        )

        self.assertEqual(
            student.name,
            "Ashok"
        )

        self.assertEqual(
            student.marks,
            [80, 90, 85]
        )

    def test_student_average(self):

        student = Student(
            1001,
            "Ashok",
            [80, 90, 85]
        )

        result = student.calculate_average()

        self.assertEqual(
            result,
            85
        )

    def test_student_grade_a(self):

        student = Student(
            1001,
            "Ashok",
            [80, 90, 85]
        )

        result = student.get_grade()

        self.assertEqual(
            result,
            "A"
        )

    def test_student_grade_b(self):

        student = Student(
            1002,
            "John",
            [70, 75, 75]
        )

        result = student.get_grade()

        self.assertEqual(
            result,
            "B"
        )

    def test_student_grade_c(self):

        student = Student(
            1003,
            "Mary",
            [60, 65, 65]
        )

        result = student.get_grade()

        self.assertEqual(
            result,
            "C"
        )

    def test_student_grade_d(self):

        student = Student(
            1004,
            "David",
            [50, 55, 55]
        )

        result = student.get_grade()

        self.assertEqual(
            result,
            "D"
        )

    def test_student_grade_f(self):

        student = Student(
            1005,
            "Peter",
            [40, 45, 45]
        )

        result = student.get_grade()

        self.assertEqual(
            result,
            "F"
        )


if __name__ == "__main__":

    unittest.main()