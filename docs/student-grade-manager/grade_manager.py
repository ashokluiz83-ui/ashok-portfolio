
from student import Student
from storage import load_students, save_students
from calculations import calculate_class_statistics


students = load_students()


def get_next_student_id():

    if len(students) == 0:

        return 1001

    return max(
        student.student_id
        for student in students
    ) + 1


def add_student():

    print("\n--- Add Student ---")

    name = input(
        "Enter student name: "
    ).strip()

    if name == "":

        print(
            "Student name cannot be empty."
        )

        return

    for student in students:

        if student.name.lower() == name.lower():

            print(
                "A student with that name already exists."
            )

            return

    while True:

        try:

            subject_count = int(
                input("How many subjects? ")
            )

            if subject_count > 0:

                break

            print(
                "Enter at least 1 subject."
            )

        except ValueError:

            print(
                "Please enter a whole number."
            )

    marks = []

    for subject in range(
        1,
        subject_count + 1
    ):

        while True:

            try:

                mark = float(
                    input(
                        f"Enter mark for subject "
                        f"{subject} (0-100): "
                    )
                )

                if 0 <= mark <= 100:

                    marks.append(mark)

                    break

                print(
                    "Please enter a mark "
                    "between 0 and 100."
                )

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    student_id = get_next_student_id()

    student = Student(
        student_id,
        name,
        marks
    )

    students.append(student)

    save_students(students)

    print(
        "\nStudent added successfully!"
    )

    student.show_info()


def show_students():

    print("\n--- All Students ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    for number, student in enumerate(
        students,
        start=1
    ):

        print(
            f"\nStudent {number}"
        )

        student.show_info()


def find_student_by_id(student_id):

    for student in students:

        if student.student_id == student_id:

            return student

    return None


def search_student():

    print("\n--- Search Student ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    while True:

        try:

            student_id = int(
                input(
                    "Enter student ID: "
                )
            )

            break

        except ValueError:

            print(
                "Please enter a valid student ID."
            )

    student = find_student_by_id(
        student_id
    )

    if student is not None:

        print("\nStudent found!")

        student.show_info()

        return

    print("Student not found.")


def remove_student():

    print("\n--- Remove Student ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    while True:

        try:

            student_id = int(
                input(
                    "Enter student ID to remove: "
                )
            )

            break

        except ValueError:

            print(
                "Please enter a valid student ID."
            )

    student = find_student_by_id(
        student_id
    )

    if student is None:

        print("Student not found.")

        return

    students.remove(student)

    save_students(students)

    print(
        f"{student.name} "
        "has been removed successfully."
    )


def edit_student():

    print("\n--- Edit Student ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    while True:

        try:

            student_id = int(
                input(
                    "Enter student ID to edit: "
                )
            )

            break

        except ValueError:

            print(
                "Please enter a valid student ID."
            )

    student = find_student_by_id(
        student_id
    )

    if student is None:

        print("Student not found.")

        return

    print(
        "\nCurrent student information:"
    )

    student.show_info()

    print(
        "\nEnter the new marks."
    )

    new_marks = []

    while True:

        try:

            subject_count = int(
                input(
                    "How many subjects? "
                )
            )

            if subject_count > 0:

                break

            print(
                "Enter at least 1 subject."
            )

        except ValueError:

            print(
                "Please enter a whole number."
            )

    for subject in range(
        1,
        subject_count + 1
    ):

        while True:

            try:

                mark = float(
                    input(
                        f"Enter mark for "
                        f"subject {subject} "
                        f"(0-100): "
                    )
                )

                if 0 <= mark <= 100:

                    new_marks.append(mark)

                    break

                print(
                    "Please enter a mark "
                    "between 0 and 100."
                )

            except ValueError:

                print(
                    "Please enter a "
                    "valid number."
                )

    student.marks = new_marks

    save_students(students)

    print(
        "\nStudent updated successfully!"
    )

    student.show_info()


def show_top_student():

    print("\n--- Top Student ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    top_student = max(
        students,
        key=lambda student:
        student.calculate_average()
    )

    print("\n🏆 Top Student")

    top_student.show_info()


def show_statistics():

    print("\n--- Class Statistics ---")

    statistics = calculate_class_statistics(
        students
    )

    if statistics["student_count"] == 0:

        print(
            "No students have been added yet."
        )

        return

    print(
        "\n=============================="
    )

    print(
        "       CLASS STATISTICS"
    )

    print(
        "=============================="
    )

    print(
        "Number of students:",
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

    print(
        "=============================="
    )


def sort_students():

    print("\n--- Sort Students ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    print(
        "\n1. Sort by name"
    )

    print(
        "2. Sort by average - highest first"
    )

    print(
        "3. Sort by average - lowest first"
    )

    choice = input(
        "\nChoose a sorting option (1-3): "
    ).strip()

    if choice == "1":

        sorted_students = sorted(
            students,
            key=lambda student:
            student.name.lower()
        )

    elif choice == "2":

        sorted_students = sorted(
            students,
            key=lambda student:
            student.calculate_average(),
            reverse=True
        )

    elif choice == "3":

        sorted_students = sorted(
            students,
            key=lambda student:
            student.calculate_average()
        )

    else:

        print(
            "Invalid sorting option."
        )

        return

    print(
        "\n--- Sorted Students ---"
    )

    for number, student in enumerate(
        sorted_students,
        start=1
    ):

        print(
            f"\nStudent {number}"
        )

        student.show_info()


def show_menu():

    print(
        "\n=============================="
    )

    print(
        "     STUDENT GRADE MANAGER"
    )

    print(
        "=============================="
    )

    print("1. Add student")

    print("2. Show all students")

    print("3. Search for a student")

    print("4. Remove a student")

    print("5. Edit student")

    print("6. Show top student")

    print("7. Show class statistics")

    print("8. Sort students")

    print("9. Exit")

    print(
        "=============================="
    )


while True:

    show_menu()

    choice = input(
        "Choose an option (1-9): "
    ).strip()

    if choice == "1":

        add_student()

    elif choice == "2":

        show_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        remove_student()

    elif choice == "5":

        edit_student()

    elif choice == "6":

        show_top_student()

    elif choice == "7":

        show_statistics()

    elif choice == "8":

        sort_students()

    elif choice == "9":

        print(
            "\nGoodbye, Ashok!"
        )

        break

    else:

        print(
            "\nInvalid choice."
            " Please choose a number from 1 to 9."
        )