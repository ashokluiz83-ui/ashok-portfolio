
import json

from student import Student


FILE_NAME = "students.json"


def load_students():

    try:

        with open(FILE_NAME, "r") as file:

            data = json.load(file)

        students = []

        next_id = 1001

        for item in data:

            student_id = item.get(
                "student_id",
                next_id
            )

            student = Student(
                student_id,
                item["name"],
                item["marks"]
            )

            students.append(student)

            if student_id >= next_id:

                next_id = student_id + 1

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
                "student_id": student.student_id,
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