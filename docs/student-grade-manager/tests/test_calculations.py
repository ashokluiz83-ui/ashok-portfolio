
import sys
from pathlib import Path
import unittest


PROJECT_FOLDER = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_FOLDER)
)


from calculations import (
    calculate_average,
    get_grade,
    calculate_class_statistics,
)


class FakeStudent:

    def __init__(
        self,
        name,
        marks
    ):

        self.name = name
        self.marks = marks

    def calculate_average(self):

        return sum(self.marks) / len(self.marks)


class TestCalculations(unittest.TestCase):

    def test_calculate_average(self):

        marks = [80, 90, 85]

        result = calculate_average(marks)

        self.assertEqual(
            result,
            85
        )

    def test_grade_a(self):

        result = get_grade(85)

        self.assertEqual(
            result,
            "A"
        )

    def test_grade_b(self):

        result = get_grade(75)

        self.assertEqual(
            result,
            "B"
        )

    def test_grade_c(self):

        result = get_grade(65)

        self.assertEqual(
            result,
            "C"
        )

    def test_grade_d(self):

        result = get_grade(55)

        self.assertEqual(
            result,
            "D"
        )

    def test_grade_f(self):

        result = get_grade(45)

        self.assertEqual(
            result,
            "F"
        )

    def test_class_statistics(self):

        students = [

            FakeStudent(
                "Ashok",
                [80, 90, 85]
            ),

            FakeStudent(
                "John",
                [60, 70, 65]
            ),

            FakeStudent(
                "Mary",
                [40, 50, 45]
            ),
        ]

        result = calculate_class_statistics(
            students
        )

        self.assertEqual(
            result["student_count"],
            3
        )

        self.assertEqual(
            result["class_average"],
            65
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

    def test_pass_percentage(self):

        students = [

            FakeStudent(
                "Ashok",
                [80, 80, 80]
            ),

            FakeStudent(
                "John",
                [40, 40, 40]
            ),
        ]

        result = calculate_class_statistics(
            students
        )

        self.assertEqual(
            result["pass_percentage"],
            50
        )

        self.assertEqual(
            result["fail_percentage"],
            50
        )

    def test_empty_class(self):

        result = calculate_class_statistics(
            []
        )

        self.assertEqual(
            result["student_count"],
            0
        )

        self.assertEqual(
            result["class_average"],
            0
        )

        self.assertEqual(
            result["passing_students"],
            0
        )

        self.assertEqual(
            result["failing_students"],
            0
        )


if __name__ == "__main__":

    unittest.main()