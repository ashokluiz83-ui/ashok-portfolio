
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

        print(
            "\nName:",
            self.name
        )

        print(
            "Marks:",
            self.marks
        )

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


student1 = Student(
    "Ashok",
    [80, 90, 85]
)

student2 = Student(
    "Mary",
    [95, 88, 92]
)

student3 = Student(
    "John",
    [65, 70, 68]
)


student1.show_info()

student2.show_info()

student3.show_info()