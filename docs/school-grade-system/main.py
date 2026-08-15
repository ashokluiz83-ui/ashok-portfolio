from student import Student

from storage import (
    load_students,
    save_students
)

from calculations import (
    calculate_class_statistics,
    get_top_student
)


students = load_students()


def get_next_student_id():

    if not students:
        return 1001

    return max(
        student.student_id
        for student in students
    ) + 1


def add_student():

    print(
        "\n=============================="
    )

    print(
        "          ADD STUDENT"
    )

    print(
        "=============================="
    )

    name = input(
        "Student name: "
    ).strip()

    if not name:

        print(
            "Name cannot be empty."
        )

        return

    class_name = input(
        "Class (example: Form 2A): "
    ).strip()

    if not class_name:

        print(
            "Class cannot be empty."
        )

        return

    try:

        subject_count = int(
            input(
                "Number of subjects: "
            )
        )

    except ValueError:

        print(
            "Please enter a valid number."
        )

        return

    if subject_count <= 0:

        print(
            "You need at least one subject."
        )

        return

    subjects = {}

    for number in range(
        1,
        subject_count + 1
    ):

        subject = input(
            f"Subject {number} name: "
        ).strip()

        if not subject:

            print(
                "Subject name cannot be empty."
            )

            return

        while True:

            try:

                mark = float(
                    input(
                        f"{subject} mark (0-100): "
                    )
                )

                if 0 <= mark <= 100:

                    subjects[
                        subject
                    ] = mark

                    break

                print(
                    "Mark must be between "
                    "0 and 100."
                )

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    student = Student(
        get_next_student_id(),
        name,
        class_name,
        subjects
    )

    students.append(
        student
    )

    save_students(
        students
    )

    print(
        "\nStudent added successfully!"
    )

    student.show_info()


def show_all_students():

    print(
        "\n=============================="
    )

    print(
        "        ALL STUDENTS"
    )

    print(
        "=============================="
    )

    if not students:

        print(
            "No students found."
        )

        return

    for student in students:

        student.show_info()


def search_student():

    print(
        "\n--- SEARCH STUDENT ---"
    )

    if not students:

        print(
            "No students found."
        )

        return

    try:

        student_id = int(
            input(
                "Enter student ID: "
            )
        )

    except ValueError:

        print(
            "Invalid student ID."
        )

        return

    for student in students:

        if student.student_id == student_id:

            print(
                "\nStudent found!"
            )

            student.show_info()

            return

    print(
        "Student not found."
    )


def remove_student():

    print(
        "\n--- REMOVE STUDENT ---"
    )

    if not students:

        print(
            "No students found."
        )

        return

    try:

        student_id = int(
            input(
                "Enter student ID: "
            )
        )

    except ValueError:

        print(
            "Invalid student ID."
        )

        return

    for student in students:

        if student.student_id == student_id:

            students.remove(
                student
            )

            save_students(
                students
            )

            print(
                "Student removed successfully."
            )

            return

    print(
        "Student not found."
    )


def show_top_student():

    print(
        "\n--- TOP STUDENT ---"
    )

    student = get_top_student(
        students
    )

    if student is None:

        print(
            "No students found."
        )

        return

    print(
        "\n🏆 Top Student"
    )

    student.show_info()


def show_statistics():

    print(
        "\n=============================="
    )

    print(
        "       CLASS STATISTICS"
    )

    print(
        "=============================="
    )

    statistics = calculate_class_statistics(
        students
    )

    if statistics[
        "student_count"
    ] == 0:

        print(
            "No students found."
        )

        return

    print(
        "Students:",
        statistics["student_count"]
    )

    print(
        "Class average:",
        round(
            statistics["class_average"],
            2
        )
    )

    print(
        "Highest average:",
        round(
            statistics["highest_average"],
            2
        )
    )

    print(
        "Lowest average:",
        round(
            statistics["lowest_average"],
            2
        )
    )

    print(
        "Passing students:",
        statistics["passing_students"]
    )

    print(
        "Failing students:",
        statistics["failing_students"]
    )

    print(
        "Pass percentage:",
        round(
            statistics["pass_percentage"],
            2
        ),
        "%"
    )

    print(
        "Fail percentage:",
        round(
            statistics["fail_percentage"],
            2
        ),
        "%"
    )


def show_menu():

    print(
        "\n=============================="
    )

    print(
        "     SCHOOL GRADE SYSTEM"
    )

    print(
        "=============================="
    )

    print(
        "1. Add student"
    )

    print(
        "2. Show all students"
    )

    print(
        "3. Search for a student"
    )

    print(
        "4. Remove a student"
    )

    print(
        "5. Show top student"
    )

    print(
        "6. Show class statistics"
    )

    print(
        "7. Exit"
    )

    print(
        "=============================="
    )


def main():

    while True:

        show_menu()

        choice = input(
            "Choose an option (1-7): "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            show_all_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            remove_student()

        elif choice == "5":

            show_top_student()

        elif choice == "6":

            show_statistics()

        elif choice == "7":

            print(
                "\nGoodbye!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


if __name__ == "__main__":

    main()