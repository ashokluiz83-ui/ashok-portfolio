
import json

from student import Student


FILE_NAME = "students.json"


def load_students():

    try:

        with open(FILE_NAME, "r") as file:

            data = json.load(file)

        students = []

        for item in data:

            student = Student(
                item["name"],
                item["marks"]
            )

            students.append(student)

        return students

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        print(
            "The student data file is damaged."
        )

        return []


def save_students(students):

    data = []

    for student in students:

        data.append(
            {
                "name": student.name,
                "marks": student.marks
            }
        )

    with open(FILE_NAME, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )