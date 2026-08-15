# School Grade Management System

A Python-based school grade management system designed as the second version of the Student Grade Manager project.

## Features

- Add students
- Automatic student IDs
- Store class information
- Store multiple subjects
- Store marks for each subject
- Calculate student averages
- Automatically assign grades
- Search students
- Edit student information
- Remove students
- Filter students by class
- Find the top student
- Calculate class statistics
- Calculate subject averages
- Export school and class reports
- JSON data storage
- Automated unit tests

## Grade System

| Average | Grade |
|---:|:---:|
| 80–100 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

## Project Structure

```text
school-grade-system/
├── main.py
├── student.py
├── calculations.py
├── storage.py
├── students.json
├── README.md
└── tests/
    ├── test_student.py
    └── test_calculations.py