
from flask import Flask, render_template, request, redirect, url_for, send_file
from io import BytesIO
from datetime import datetime

from student import Student
from storage import load_students, save_students


app = Flask(__name__)


@app.route("/")
def dashboard():

    students = load_students()

    return render_template(
        "index.html",
        students=students
    )


@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"].strip()

        class_name = request.form["class_name"].strip()

        subjects = {}

        subject_names = request.form.getlist("subject_name")
        subject_marks = request.form.getlist("subject_mark")

        for subject_name, mark in zip(
            subject_names,
            subject_marks
        ):

            subject_name = subject_name.strip()

            if subject_name:

                subjects[subject_name] = float(mark)

        students = load_students()

        if students:

            next_id = max(
                student.student_id
                for student in students
            ) + 1

        else:

            next_id = 1001

        student = Student(
            next_id,
            name,
            class_name,
            subjects
        )

        students.append(student)

        save_students(students)

        return redirect(
            url_for(
                "student_details",
                student_id=student.student_id
            )
        )

    return render_template(
        "add_student.html"
    )


@app.route("/students")
def view_students():

    students = load_students()

    return render_template(
        "students.html",
        students=students
    )


@app.route("/search")
def search_student():

    query = request.args.get(
        "query",
        ""
    ).strip().lower()

    students = load_students()

    results = []

    if query:

        for student in students:

            student_id = str(
                student.student_id
            )

            name = student.name.lower()

            class_name = student.class_name.lower()

            if (
                query in student_id
                or query in name
                or query in class_name
            ):

                results.append(student)

    return render_template(
        "search.html",
        results=results,
        query=query
    )


@app.route(
    "/student/<int:student_id>/edit",
    methods=["GET", "POST"]
)
def edit_student(student_id):

    students = load_students()

    student = next(
        (
            student
            for student in students
            if student.student_id == student_id
        ),
        None
    )

    if student is None:

        return "Student not found", 404

    if request.method == "POST":

        student.name = request.form[
            "name"
        ].strip()

        student.class_name = request.form[
            "class_name"
        ].strip()

        subjects = {}

        subject_names = request.form.getlist(
            "subject_name"
        )

        subject_marks = request.form.getlist(
            "subject_mark"
        )

        for subject_name, mark in zip(
            subject_names,
            subject_marks
        ):

            subject_name = subject_name.strip()

            if subject_name:

                subjects[
                    subject_name
                ] = float(mark)

        student.subjects = subjects

        save_students(students)

        return redirect(
            url_for(
                "student_details",
                student_id=student.student_id
            )
        )

    return render_template(
        "edit_student.html",
        student=student
    )


@app.route(
    "/student/<int:student_id>/delete",
    methods=["POST"]
)
def delete_student(student_id):

    students = load_students()

    students = [
        student
        for student in students
        if student.student_id != student_id
    ]

    save_students(students)

    return redirect(
        url_for(
            "view_students"
        )
    )


@app.route("/student/<int:student_id>")
def student_details(student_id):

    students = load_students()

    student = next(
        (
            student
            for student in students
            if student.student_id == student_id
        ),
        None
    )

    if student is None:

        return "Student not found", 404

    return render_template(
        "student_details.html",
        student=student
    )


@app.route("/classes")
def classes():

    students = load_students()

    class_groups = {}

    for student in students:

        class_name = student.class_name

        if class_name not in class_groups:

            class_groups[class_name] = []

        class_groups[class_name].append(
            student
        )

    class_data = {}

    for class_name, class_students in class_groups.items():

        averages = [
            student.calculate_average()
            for student in class_students
        ]

        if averages:

            class_average = (
                sum(averages)
                / len(averages)
            )

            highest_average = max(averages)

            lowest_average = min(averages)

            passing = [
                average
                for average in averages
                if average >= 50
            ]

            failing = [
                average
                for average in averages
                if average < 50
            ]

            pass_percentage = (
                len(passing)
                / len(averages)
                * 100
            )

            fail_percentage = (
                len(failing)
                / len(averages)
                * 100
            )

        else:

            class_average = 0
            highest_average = 0
            lowest_average = 0
            passing = []
            failing = []
            pass_percentage = 0
            fail_percentage = 0

        class_data[class_name] = {

            "students": class_students,

            "average": class_average,

            "highest": highest_average,

            "lowest": lowest_average,

            "passing": len(passing),

            "failing": len(failing),

            "pass_percentage": pass_percentage,

            "fail_percentage": fail_percentage

        }

    class_data = dict(
        sorted(
            class_data.items()
        )
    )

    return render_template(
        "classes.html",
        class_data=class_data
    )


@app.route("/class/<path:class_name>")
def class_students(class_name):

    students = load_students()

    class_students_list = [
        student
        for student in students
        if student.class_name.lower()
        == class_name.lower()
    ]

    class_students_list.sort(
        key=lambda student:
        student.name.lower()
    )

    class_average = 0
    highest_average = 0
    lowest_average = 0
    passing = 0
    failing = 0
    pass_percentage = 0
    fail_percentage = 0

    if class_students_list:

        averages = [
            student.calculate_average()
            for student in class_students_list
        ]

        class_average = (
            sum(averages)
            / len(averages)
        )

        highest_average = max(
            averages
        )

        lowest_average = min(
            averages
        )

        passing = sum(
            1
            for average in averages
            if average >= 50
        )

        failing = sum(
            1
            for average in averages
            if average < 50
        )

        pass_percentage = (
            passing
            / len(averages)
            * 100
        )

        fail_percentage = (
            failing
            / len(averages)
            * 100
        )

    return render_template(
        "class_students.html",
        class_name=class_name,
        students=class_students_list,
        class_average=class_average,
        highest_average=highest_average,
        lowest_average=lowest_average,
        passing=passing,
        failing=failing,
        pass_percentage=pass_percentage,
        fail_percentage=fail_percentage
    )


@app.route(
    "/class/<path:class_name>/report"
)
def class_report(class_name):

    students = load_students()

    class_students_list = [
        student
        for student in students
        if student.class_name.lower()
        == class_name.lower()
    ]

    class_students_list.sort(
        key=lambda student:
        student.calculate_average(),
        reverse=True
    )

    averages = [
        student.calculate_average()
        for student in class_students_list
    ]

    if averages:

        class_average = (
            sum(averages)
            / len(averages)
        )

        highest_average = max(
            averages
        )

        lowest_average = min(
            averages
        )

        passing = sum(
            1
            for average in averages
            if average >= 50
        )

        failing = sum(
            1
            for average in averages
            if average < 50
        )

        pass_percentage = (
            passing
            / len(averages)
            * 100
        )

        fail_percentage = (
            failing
            / len(averages)
            * 100
        )

    else:

        class_average = 0
        highest_average = 0
        lowest_average = 0
        passing = 0
        failing = 0
        pass_percentage = 0
        fail_percentage = 0

    return render_template(
        "class_report.html",
        class_name=class_name,
        students=class_students_list,
        class_average=class_average,
        highest_average=highest_average,
        lowest_average=lowest_average,
        passing=passing,
        failing=failing,
        pass_percentage=pass_percentage,
        fail_percentage=fail_percentage,
        generated_at=datetime.now()
    )


@app.route(
    "/class/<path:class_name>/report/download"
)
def download_class_report(class_name):

    students = load_students()

    class_students_list = [
        student
        for student in students
        if student.class_name.lower()
        == class_name.lower()
    ]

    class_students_list.sort(
        key=lambda student:
        student.calculate_average(),
        reverse=True
    )

    averages = [
        student.calculate_average()
        for student in class_students_list
    ]

    if averages:

        class_average = (
            sum(averages)
            / len(averages)
        )

        highest_average = max(
            averages
        )

        lowest_average = min(
            averages
        )

        passing = sum(
            1
            for average in averages
            if average >= 50
        )

        failing = sum(
            1
            for average in averages
            if average < 50
        )

        pass_percentage = (
            passing
            / len(averages)
            * 100
        )

        fail_percentage = (
            failing
            / len(averages)
            * 100
        )

    else:

        class_average = 0
        highest_average = 0
        lowest_average = 0
        passing = 0
        failing = 0
        pass_percentage = 0
        fail_percentage = 0

    lines = []

    lines.append(
        "SCHOOL GRADE SYSTEM"
    )

    lines.append(
        "=" * 50
    )

    lines.append(
        f"CLASS REPORT: {class_name}"
    )

    lines.append(
        "=" * 50
    )

    lines.append(
        f"Report generated: {datetime.now()}"
    )

    lines.append("")

    lines.append(
        f"Number of students: "
        f"{len(class_students_list)}"
    )

    lines.append(
        f"Class average: "
        f"{class_average:.2f}"
    )

    lines.append(
        f"Highest average: "
        f"{highest_average:.2f}"
    )

    lines.append(
        f"Lowest average: "
        f"{lowest_average:.2f}"
    )

    lines.append(
        f"Passing students: "
        f"{passing}"
    )

    lines.append(
        f"Failing students: "
        f"{failing}"
    )

    lines.append(
        f"Pass percentage: "
        f"{pass_percentage:.2f}%"
    )

    lines.append(
        f"Fail percentage: "
        f"{fail_percentage:.2f}%"
    )

    lines.append("")

    lines.append(
        "STUDENT RESULTS"
    )

    lines.append(
        "=" * 50
    )

    for position, student in enumerate(
        class_students_list,
        start=1
    ):

        lines.append("")

        lines.append(
            f"Position: {position}"
        )

        lines.append(
            f"Student ID: "
            f"{student.student_id}"
        )

        lines.append(
            f"Name: {student.name}"
        )

        lines.append(
            f"Class: {student.class_name}"
        )

        lines.append(
            "Subjects:"
        )

        for subject, mark in student.subjects.items():

            lines.append(
                f"  {subject}: "
                f"{mark:.2f}"
            )

        lines.append(
            f"Average: "
            f"{student.calculate_average():.2f}"
        )

        lines.append(
            f"Grade: "
            f"{student.get_grade()}"
        )

        lines.append(
            "-" * 50
        )

    report_text = "\n".join(
        lines
    )

    file = BytesIO()

    file.write(
        report_text.encode(
            "utf-8"
        )
    )

    file.seek(0)

    safe_class_name = (
        class_name
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
    )

    filename = (
        f"class_{safe_class_name}_report.txt"
    )

    return send_file(
        file,
        as_attachment=True,
        download_name=filename,
        mimetype="text/plain"
    )


@app.route("/statistics")
def statistics():

    students = load_students()

    if not students:

        statistics_data = {
            "count": 0,
            "average": 0,
            "highest": 0,
            "lowest": 0,
            "passing": 0,
            "failing": 0,
            "pass_percentage": 0,
            "fail_percentage": 0
        }

    else:

        averages = [
            student.calculate_average()
            for student in students
        ]

        passing = [
            average
            for average in averages
            if average >= 50
        ]

        failing = [
            average
            for average in averages
            if average < 50
        ]

        statistics_data = {

            "count": len(students),

            "average":
                sum(averages)
                / len(averages),

            "highest":
                max(averages),

            "lowest":
                min(averages),

            "passing":
                len(passing),

            "failing":
                len(failing),

            "pass_percentage":
                len(passing)
                / len(students)
                * 100,

            "fail_percentage":
                len(failing)
                / len(students)
                * 100

        }

    return render_template(
        "statistics.html",
        statistics=statistics_data
    )


@app.route("/top-student")
def top_student():

    students = load_students()

    if not students:

        return render_template(
            "top_student.html",
            student=None
        )

    student = max(
        students,
        key=lambda student:
        student.calculate_average()
    )

    return render_template(
        "top_student.html",
        student=student
    )


@app.route("/subject-average")
def subject_average():

    students = load_students()

    subject_marks = {}

    for student in students:

        for subject, mark in student.subjects.items():

            if subject not in subject_marks:

                subject_marks[subject] = []

            subject_marks[subject].append(
                mark
            )

    averages = {}

    for subject, marks in subject_marks.items():

        averages[subject] = (
            sum(marks)
            / len(marks)
        )

    return render_template(
        "subject_average.html",
        averages=averages
    )


@app.route("/report")
def report():

    students = load_students()

    return render_template(
        "report.html",
        students=students,
        generated_at=datetime.now()
    )


@app.route("/report/download")
def download_report():

    students = load_students()

    lines = []

    lines.append(
        "SCHOOL GRADE SYSTEM"
    )

    lines.append(
        "=" * 40
    )

    lines.append(
        f"Report generated: {datetime.now()}"
    )

    lines.append("")

    for student in students:

        lines.append(
            "-" * 40
        )

        lines.append(
            f"Student ID: {student.student_id}"
        )

        lines.append(
            f"Name: {student.name}"
        )

        lines.append(
            f"Class: {student.class_name}"
        )

        lines.append("")

        lines.append(
            "Subjects:"
        )

        for subject, mark in student.subjects.items():

            lines.append(
                f"  {subject}: {mark}"
            )

        lines.append("")

        lines.append(
            f"Average: "
            f"{student.calculate_average():.2f}"
        )

        lines.append(
            f"Grade: {student.get_grade()}"
        )

        lines.append("")

    report_text = "\n".join(
        lines
    )

    file = BytesIO()

    file.write(
        report_text.encode(
            "utf-8"
        )
    )

    file.seek(0)

    return send_file(
        file,
        as_attachment=True,
        download_name="school_grade_report.txt",
        mimetype="text/plain"
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )