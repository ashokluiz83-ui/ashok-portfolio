def calculate_average(subjects):

    if not subjects:
        return 0

    return sum(
        subjects.values()
    ) / len(subjects)


def get_grade(average):

    if average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    return "F"


def calculate_class_statistics(students):

    if not students:

        return {
            "student_count": 0,
            "class_average": 0,
            "highest_average": 0,
            "lowest_average": 0,
            "passing_students": 0,
            "failing_students": 0,
            "pass_percentage": 0,
            "fail_percentage": 0
        }

    averages = [
        student.calculate_average()
        for student in students
    ]

    count = len(students)

    class_average = sum(averages) / count

    highest_average = max(averages)

    lowest_average = min(averages)

    passing_students = sum(
        1
        for average in averages
        if average >= 50
    )

    failing_students = count - passing_students

    pass_percentage = (
        passing_students / count
    ) * 100

    fail_percentage = (
        failing_students / count
    ) * 100

    return {
        "student_count": count,
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "passing_students": passing_students,
        "failing_students": failing_students,
        "pass_percentage": pass_percentage,
        "fail_percentage": fail_percentage
    }


def get_top_student(students):

    if not students:
        return None

    return max(
        students,
        key=lambda student:
        student.calculate_average()
    )


def get_students_by_class(
    students,
    class_name
):

    return [
        student
        for student in students
        if student.class_name.lower()
        == class_name.lower()
    ]


def get_subject_average(
    students,
    subject
):

    marks = []

    for student in students:

        for student_subject, mark in (
            student.subjects.items()
        ):

            if (
                student_subject.lower()
                == subject.lower()
            ):

                marks.append(mark)

    if not marks:
        return 0

    return sum(marks) / len(marks)