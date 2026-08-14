
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
)


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


if __name__ == "__main__":

    unittest.main()