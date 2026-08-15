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

from calculations import (
    calculate_average,
    get_grade,
    calculate_class_statistics,
    get_top_student,
    get_students_by_class,
    get_subject_average
)


class TestCalculations(unittest.TestCase):

    def setUp(self):

        self.students = [

            Student(
                1001,
                "Ashok",
                "Form 2A",
                {
                    "Mathematics": 80,
                    "English": 90
                }
            ),

            Student(
                1002,
                "John",
                "Form 2A",
                {
                    "Mathematics": 60,
                    "English": 70
                }
            ),

            Student(
                1003,
                "Mary",
                "Form 2B",
                {
                    "Mathematics": 40,
                    "English": 50
                }
            )
        ]

    def test_average(self):

        result = calculate_average(
            {
                "Math": 80,
                "English": 90
            }
        )

        self.assertEqual(
            result,
            85
        )

    def test_grade(self):

        self.assertEqual(
            get_grade(85),
            "A"
        )

        self.assertEqual(
            get_grade(75),
            "B"
        )

        self.assertEqual(
            get_grade(65),
            "C"
        )

        self.assertEqual(
            get_grade(55),
            "D"
        )

        self.assertEqual(
            get_grade(45),
            "F"
        )

    def test_class_statistics(self):

        result = calculate_class_statistics(
            self.students
        )

        self.assertEqual(
            result["student_count"],
            3
        )

        self.assertEqual(
            result["highest_average"],
            85
        )

        self.assertEqual(
            result["lowest_average"],
            45
        )

        self.assertEqual(
            result["passing_students"],
            2
        )

        self.assertEqual(
            result["failing_students"],
            1
        )

    def test_top_student(self):

        student = get_top_student(
            self.students
        )

        self.assertEqual(
            student.name,
            "Ashok"
        )

    def test_students_by_class(self):

        result = get_students_by_class(
            self.students,
            "Form 2A"
        )

        self.assertEqual(
            len(result),
            2
        )

    def test_subject_average(self):

        result = get_subject_average(
            self.students,
            "Mathematics"
        )

        self.assertEqual(
            result,
            60
        )

    def test_empty_statistics(self):

        result = calculate_class_statistics(
            []
        )

        self.assertEqual(
            result["student_count"],
            0
        )


if __name__ == "__main__":
    unittest.main()