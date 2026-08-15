import json
from pathlib import Path

from student import Student


BASE_FOLDER = Path(__file__).resolve().parent

FILE_NAME = BASE_FOLDER / "students.json"


def load_students():

    try:

        with open(
            FILE_NAME,
            "r"
        ) as file:

            data = json.load(file)

        students = []

        for item in data:

            student = Student(
                item["student_id"],
                item["name"],
                item["class_name"],
                item["subjects"]
            )

            students.append(student)

        return students

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        print(
            "Student data file is damaged."
        )

        return []


def save_students(students):

    data = []

    for student in students:

        data.append(
            {
                "student_id":
                    student.student_id,

                "name":
                    student.name,

                "class_name":
                    student.class_name,

                "subjects":
                    student.subjects
            }
        )

    with open(
        FILE_NAME,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )