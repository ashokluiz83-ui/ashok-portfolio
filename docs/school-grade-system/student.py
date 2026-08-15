class Student:

    def __init__(
        self,
        student_id,
        name,
        class_name,
        subjects
    ):

        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.subjects = subjects

    def calculate_average(self):

        if not self.subjects:
            return 0

        total = sum(
            self.subjects.values()
        )

        return total / len(
            self.subjects
        )

    def get_grade(self):

        average = self.calculate_average()

        if average >= 80:
            return "A"

        elif average >= 70:
            return "B"

        elif average >= 60:
            return "C"

        elif average >= 50:
            return "D"

        else:
            return "F"

    def show_info(self):

        print(
            "\n------------------------------"
        )

        print(
            "Student ID:",
            self.student_id
        )

        print(
            "Name:",
            self.name
        )

        print(
            "Class:",
            self.class_name
        )

        print(
            "\nSubjects:"
        )

        for subject, mark in self.subjects.items():

            print(
                f"  {subject}: {mark}"
            )

        print(
            "\nAverage:",
            round(
                self.calculate_average(),
                2
            )
        )

        print(
            "Grade:",
            self.get_grade()
        )

        print(
            "------------------------------"
        )