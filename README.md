# Student Grade Manager

A beginner-friendly Python application for managing student marks, calculating averages, assigning grades, searching students, removing students, and finding the top-performing student.

## Features

* Add students
* Enter any number of subjects
* Calculate student averages
* Automatically assign grades
* Display all students
* Search for a student
* Remove a student
* Find the top student
* Save student data permanently using JSON
* Load saved student data when the program starts
* Validate user input

## Grade System

| Average | Grade |
| ------: | :---: |
|  80–100 |   A   |
|   70–79 |   B   |
|   60–69 |   C   |
|   50–59 |   D   |
|    0–49 |   F   |

## Project Structure

```text
student-grade-manager/
│
├── grade_manager.py
└── students.json
```

## Requirements

* Python 3.14 or newer
* VS Code or another code editor

## How to Run

Open the project in VS Code.

Open the terminal and run:

```powershell
py docs\student-grade-manager\grade_manager.py
```

The program will display a menu:

```text
1. Add student
2. Show all students
3. Search for a student
4. Remove a student
5. Show top student
6. Exit
```

Choose an option by entering the corresponding number.

## Data Storage

The program uses a JSON file called `students.json` to store student information.

This means student data remains available after the program is closed and started again.

## What I Learned

This project helped me practice:

* Variables
* Strings
* Numbers
* Lists
* Dictionaries
* Functions
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* `try` and `except`
* File handling
* JSON
* Searching data
* Removing data
* Finding maximum values
* Git
* GitHub

## Author

**Ashok**

Learning Python and working toward becoming a programmer.

## Project Status

**Completed beginner project**

More features will be added as I continue learning Python.
