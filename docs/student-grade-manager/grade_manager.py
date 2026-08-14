from calculations import calculate_average, get_grade
from storage import load_students, save_students


students = load_students()


def add_student():

    print("\n--- Add Student ---")

    name = input(
        "Enter student name: "
    ).strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    while True:

        try:

            subject_count = int(
                input("How many subjects? ")
            )

            if subject_count > 0:
                break

            print("Enter at least 1 subject.")

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

    average = calculate_average(marks)

    grade = get_grade(average)

    student = {
        "name": name,
        "marks": marks,
        "average": average,
        "grade": grade
    }

    students.append(student)

    save_students(students)

    print("\nStudent added successfully!")

    print("Name:", name)

    print(
        "Average:",
        round(average, 2)
    )

    print("Grade:", grade)


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
            "\nStudent",
            number
        )

        print(
            "Name:",
            student["name"]
        )

        print(
            "Marks:",
            student["marks"]
        )

        print(
            "Average:",
            round(
                student["average"],
                2
            )
        )

        print(
            "Grade:",
            student["grade"]
        )


def search_student():

    print("\n--- Search Student ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    search_name = input(
        "Enter the student's name: "
    ).strip().lower()

    found = False

    for student in students:

        if (
            student["name"].lower()
            == search_name
        ):

            print("\nStudent found!")

            print(
                "Name:",
                student["name"]
            )

            print(
                "Marks:",
                student["marks"]
            )

            print(
                "Average:",
                round(
                    student["average"],
                    2
                )
            )

            print(
                "Grade:",
                student["grade"]
            )

            found = True

            break

    if not found:

        print("Student not found.")


def remove_student():

    print("\n--- Remove Student ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    remove_name = input(
        "Enter the student's name to remove: "
    ).strip().lower()

    for student in students:

        if (
            student["name"].lower()
            == remove_name
        ):

            students.remove(student)

            save_students(students)

            print(
                f"{student['name']} "
                "has been removed successfully."
            )

            return

    print("Student not found.")


def show_top_student():

    print("\n--- Top Student ---")

    if len(students) == 0:

        print(
            "No students have been added yet."
        )

        return

    top_student = max(
        students,
        key=lambda student: student["average"]
    )

    print("\n🏆 Top Student")

    print(
        "Name:",
        top_student["name"]
    )

    print(
        "Average:",
        round(
            top_student["average"],
            2
        )
    )

    print(
        "Grade:",
        top_student["grade"]
    )


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

    print("5. Show top student")

    print("6. Exit")

    print(
        "=============================="
    )


while True:

    show_menu()

    choice = input(
        "Choose an option (1-6): "
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

        show_top_student()

    elif choice == "6":

        print("\nGoodbye, Ashok!")

        break

    else:

        print(
            "\nInvalid choice."
            " Please choose 1, 2, 3, 4, 5, or 6."
        )