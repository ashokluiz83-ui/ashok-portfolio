def calculate_average(marks):

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


def get_grade(average):

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


def calculate_class_statistics(students):

    if len(students) == 0:

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

    averages = []

    for student in students:

        averages.append(
            student.calculate_average()
        )

    student_count = len(students)

    class_average = (
        sum(averages)
        / student_count
    )

    highest_average = max(averages)

    lowest_average = min(averages)

    passing_students = 0
    failing_students = 0

    for student in students:

        if student.calculate_average() >= 50:
            passing_students += 1

        else:
            failing_students += 1

    pass_percentage = (
        passing_students
        / student_count
    ) * 100

    fail_percentage = (
        failing_students
        / student_count
    ) * 100

    return {
        "student_count": student_count,
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "passing_students": passing_students,
        "failing_students": failing_students,
        "pass_percentage": pass_percentage,
        "fail_percentage": fail_percentage
    }