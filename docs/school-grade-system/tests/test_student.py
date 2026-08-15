import sys
from pathlib import Path
import unittest


PROJECT_FOLDER = (
    Path(__file__).resolve().parent.parent
)

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
            "Form 2A",
            {
                "Mathematics": 80,
                "English": 75
            }
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
            student.class_name,
            "Form 2A"
        )

    def test_average(self):

        student = Student(
            1001,
            "Ashok",
            "Form 2A",
            {
                "Mathematics": 80,
                "English": 90
            }
        )

        self.assertEqual(
            student.calculate_average(),
            85
        )

    def test_grade_a(self):

        student = Student(
            1001,
            "Ashok",
            "Form 2A",
            {
                "Mathematics": 80
            }
        )

        self.assertEqual(
            student.get_grade(),
            "A"
        )

    def test_grade_b(self):

        student = Student(
            1001,
            "Ashok",
            "Form 2A",
            {
                "Mathematics": 70
            }
        )

        self.assertEqual(
            student.get_grade(),
            "B"
        )

    def test_grade_c(self):

        student = Student(
            1001,
            "Ashok",
            "Form 2A",
            {
                "Mathematics": 60
            }
        )

        self.assertEqual(
            student.get_grade(),
            "C"
        )

    def test_grade_d(self):

        student = Student(
            1001,
            "Ashok",
            "Form 2A",
            {
                "Mathematics": 50
            }
        )

        self.assertEqual(
            student.get_grade(),
            "D"
        )

    def test_grade_f(self):

        student = Student(
            1001,
            "Ashok",
            "Form 2A",
            {
                "Mathematics": 40
            }
        )

        self.assertEqual(
            student.get_grade(),
            "F"
        )

    def test_empty_subjects(self):

        student = Student(
            1001,
            "Ashok",
            "Form 2A",
            {}
        )

        self.assertEqual(
            student.calculate_average(),
            0
        )

        self.assertEqual(
            student.get_grade(),
            "F"
        )


if __name__ == "__main__":
    unittest.main()