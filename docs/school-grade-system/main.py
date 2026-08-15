from student import Student

from storage import (
    load_students,
    save_students
)

from calculations import (
    calculate_class_statistics,
    get_top_student,
    get_students_by_class,
    get_subject_average
)


students = load_students()


def get_next_student_id():

    if not students:
        return 1001

    return max(
        student.student_id
        for student in students
    ) + 1


def find_student(student_id):

    for student in students:

        if student.student_id == student_id:
            return student

    return None


def get_mark(subject):

    while True:

        try:

            mark = float(
                input(
                    f"{subject} mark (0-100): "
                )
            )

            if 0 <= mark <= 100:
                return mark

            print(
                "Mark must be between 0 and 100."
            )

        except ValueError:

            print(
                "Please enter a valid number."
            )


def add_student():

    print("\n==============================")
    print("          ADD STUDENT")
    print("==============================")

    name = input(
        "Student name: "
    ).strip()

    if not name:

        print("Name cannot be empty.")
        return

    class_name = input(
        "Class (example: Form 2A): "
    ).strip()

    if not class_name:

        print("Class cannot be empty.")
        return

    try:

        subject_count = int(
            input("Number of subjects: ")
        )

    except ValueError:

        print("Please enter a valid number.")
        return

    if subject_count <= 0:

        print("At least one subject is required.")
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

            print("Subject name cannot be empty.")
            return

        if subject in subjects:

            print(
                "That subject has already been added."
            )

            return

        subjects[subject] = get_mark(subject)

    student = Student(
        get_next_student_id(),
        name,
        class_name,
        subjects
    )

    students.append(student)

    save_students(students)

    print(
        "\nStudent added successfully!"
    )

    student.show_info()


def show_all_students():

    print("\n==============================")
    print("        ALL STUDENTS")
    print("==============================")

    if not students:

        print("No students found.")
        return

    for student in students:

        student.show_info()


def search_student():

    print("\n--- SEARCH STUDENT ---")

    if not students:

        print("No students found.")
        return

    try:

        student_id = int(
            input("Enter student ID: ")
        )

    except ValueError:

        print("Invalid student ID.")
        return

    student = find_student(student_id)

    if student:

        print("\nStudent found!")
        student.show_info()

    else:

        print("Student not found.")


def edit_student():

    print("\n--- EDIT STUDENT ---")

    if not students:

        print("No students found.")
        return

    try:

        student_id = int(
            input("Enter student ID: ")
        )

    except ValueError:

        print("Invalid student ID.")
        return

    student = find_student(student_id)

    if not student:

        print("Student not found.")
        return

    print("\nCurrent information:")
    student.show_info()

    new_name = input(
        "\nNew name "
        "(press Enter to keep current): "
    ).strip()

    if new_name:

        student.name = new_name

    new_class = input(
        "New class "
        "(press Enter to keep current): "
    ).strip()

    if new_class:

        student.class_name = new_class

    choice = input(
        "\nReplace subject marks? (y/n): "
    ).strip().lower()

    if choice == "y":

        try:

            subject_count = int(
                input("Number of subjects: ")
            )

        except ValueError:

            print("Invalid number.")
            return

        if subject_count <= 0:

            print("At least one subject is required.")
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

            subjects[subject] = get_mark(subject)

        student.subjects = subjects

    save_students(students)

    print(
        "\nStudent updated successfully!"
    )

    student.show_info()


def remove_student():

    print("\n--- REMOVE STUDENT ---")

    if not students:

        print("No students found.")
        return

    try:

        student_id = int(
            input("Enter student ID: ")
        )

    except ValueError:

        print("Invalid student ID.")
        return

    student = find_student(student_id)

    if not student:

        print("Student not found.")
        return

    confirmation = input(
        f"Remove {student.name}? (y/n): "
    ).strip().lower()

    if confirmation != "y":

        print("Removal cancelled.")
        return

    students.remove(student)

    save_students(students)

    print(
        "Student removed successfully."
    )


def show_class_students():

    print("\n--- CLASS STUDENTS ---")

    if not students:

        print("No students found.")
        return

    class_name = input(
        "Enter class name: "
    ).strip()

    class_students = get_students_by_class(
        students,
        class_name
    )

    if not class_students:

        print(
            "No students found in that class."
        )

        return

    print(
        f"\nStudents in {class_name}:"
    )

    for student in class_students:

        student.show_info()


def show_top_student_menu():

    print("\n--- TOP STUDENT ---")

    if not students:

        print("No students found.")
        return

    class_name = input(
        "Enter class name "
        "(or press Enter for whole school): "
    ).strip()

    if class_name:

        selected_students = get_students_by_class(
            students,
            class_name
        )

    else:

        selected_students = students

    if not selected_students:

        print(
            "No students found."
        )

        return

    top_student = get_top_student(
        selected_students
    )

    print("\n🏆 Top Student")

    top_student.show_info()


def show_statistics():

    print("\n--- CLASS STATISTICS ---")

    class_name = input(
        "Enter class name "
        "(or press Enter for whole school): "
    ).strip()

    if class_name:

        selected_students = get_students_by_class(
            students,
            class_name
        )

    else:

        selected_students = students

    statistics = calculate_class_statistics(
        selected_students
    )

    if statistics["student_count"] == 0:

        print("No students found.")
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


def show_subject_average():

    print("\n--- SUBJECT PERFORMANCE ---")

    if not students:

        print("No students found.")
        return

    subject = input(
        "Enter subject name: "
    ).strip()

    average = get_subject_average(
        students,
        subject
    )

    if average == 0:

        print(
            "No marks found for that subject."
        )

        return

    print(
        f"\n{subject} average:",
        round(average, 2)
    )


def export_report():

    print("\n--- EXPORT REPORT ---")

    class_name = input(
        "Enter class name "
        "(or press Enter for whole school): "
    ).strip()

    if class_name:

        selected_students = get_students_by_class(
            students,
            class_name
        )

        report_name = (
            f"report_{class_name.replace(' ', '_')}.txt"
        )

    else:

        selected_students = students

        report_name = "school_report.txt"

    if not selected_students:

        print("No students found.")
        return

    statistics = calculate_class_statistics(
        selected_students
    )

    try:

        with open(
            report_name,
            "w"
        ) as file:

            file.write(
                "================================\n"
            )

            file.write(
                "       SCHOOL GRADE REPORT\n"
            )

            file.write(
                "================================\n\n"
            )

            if class_name:

                file.write(
                    f"Class: {class_name}\n\n"
                )

            for student in selected_students:

                file.write(
                    f"ID: {student.student_id}\n"
                )

                file.write(
                    f"Name: {student.name}\n"
                )

                file.write(
                    f"Class: {student.class_name}\n"
                )

                file.write(
                    "Subjects:\n"
                )

                for subject, mark in (
                    student.subjects.items()
                ):

                    file.write(
                        f"  {subject}: {mark}\n"
                    )

                file.write(
                    f"Average: "
                    f"{student.calculate_average():.2f}\n"
                )

                file.write(
                    f"Grade: {student.get_grade()}\n"
                )

                file.write(
                    "--------------------------------\n"
                )

            file.write(
                "\nCLASS STATISTICS\n"
            )

            file.write(
                f"Students: "
                f"{statistics['student_count']}\n"
            )

            file.write(
                f"Average: "
                f"{statistics['class_average']:.2f}\n"
            )

            file.write(
                f"Highest: "
                f"{statistics['highest_average']:.2f}\n"
            )

            file.write(
                f"Lowest: "
                f"{statistics['lowest_average']:.2f}\n"
            )

            file.write(
                f"Pass rate: "
                f"{statistics['pass_percentage']:.2f}%\n"
            )

        print(
            f"\nReport created: {report_name}"
        )

    except OSError as error:

        print(
            f"Could not create report: {error}"
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

    print("1. Add student")
    print("2. Show all students")
    print("3. Search for a student")
    print("4. Edit student")
    print("5. Remove student")
    print("6. Show students by class")
    print("7. Show top student")
    print("8. Show class statistics")
    print("9. Show subject average")
    print("10. Export report")
    print("11. Exit")

    print(
        "=============================="
    )


def main():

    while True:

        show_menu()

        choice = input(
            "Choose an option (1-11): "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            show_all_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            edit_student()

        elif choice == "5":

            remove_student()

        elif choice == "6":

            show_class_students()

        elif choice == "7":

            show_top_student_menu()

        elif choice == "8":

            show_statistics()

        elif choice == "9":

            show_subject_average()

        elif choice == "10":

            export_report()

        elif choice == "11":

            print(
                "\nGoodbye, Ashok!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


if __name__ == "__main__":
    main()