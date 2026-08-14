
class Student:

    def __init__(self, name, marks):

        self.name = name

        self.marks = marks


    def calculate_average(self):

        return sum(self.marks) / len(self.marks)


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

        print("\nName:", self.name)

        print("Marks:", self.marks)

        print(
            "Average:",
            round(
                self.calculate_average(),
                2
            )
        )

        print(
            "Grade:",
            self.get_grade()
        )