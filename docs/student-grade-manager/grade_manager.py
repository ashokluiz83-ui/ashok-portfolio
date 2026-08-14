
from student import Student
from storage import load_students, save_students


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

    print("7. Exit")

    print(
        "=============================="
    )


while True:

    show_menu()

    choice = input(
        "Choose an option (1-7): "
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

        print(
            "\nGoodbye, Ashok!"
        )

        break

    else:

        print(
            "\nInvalid choice."
            " Please choose 1, 2, 3, 4, 5, 6, or 7."
        )