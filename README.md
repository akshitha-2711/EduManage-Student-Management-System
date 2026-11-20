# EduManage – Student Management System

A responsive student management dashboard for managing academic records, tracking student performance, and visualizing academic insights. EduManage combines a modern web interface with JSON-based data storage and a Python command-line application.

---

## Overview

Educational institutions often manage student information using manual registers or scattered spreadsheets. This can make it difficult to maintain accurate records, search for information, and analyze academic performance.

**EduManage** provides a simple solution through an interactive dashboard that allows administrators and academic coordinators to manage student records, monitor academic performance, and visualize important statistics.

The project is designed to be lightweight and easy to run locally without requiring a complex database setup.

## Features

### 1. Login and Authentication
- Clean and responsive login interface.
- Password visibility toggle.
- Demo login credentials for quick access.
- Session handling using browser localStorage.
- Sign-out functionality.

### 2. Student Management
- Add new student records.
- View all registered students.
- Search students by ID, name, or branch.
- Filter records by branch.
- Sort student records.
- Edit existing student information.
- Delete student records.
- Input validation to prevent invalid entries.

### 3. Academic Dashboard

The dashboard displays key academic performance indicators:

- **Total Students:** Number of registered students.
- **Average Marks:** Average marks across all students.
- **Highest Marks:** Highest score and the corresponding student.
- **Pass Rate:** Percentage of students scoring 40 marks or above.

### 4. Data Visualization

Interactive charts provide insights into student performance:

- Student Marks Overview – Area chart.
- Branch Distribution – Doughnut chart.
- Score Brackets – Bar chart.
- Branch Performance – Progress indicators.

### 5. Data Management
- Store student records in JSON format.
- Import existing `students.json` files.
- Export updated student records.
- Persist application data using browser localStorage.
- Share a common JSON data format with the Python CLI.

### 6. Python CLI
A separate Python command-line application provides basic student record management through the terminal.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Command-line student management and local development server |
| HTML5 | Structure of the login page and dashboard |
| Tailwind CSS | Responsive styling and user interface design |
| JavaScript | Application logic, validation, search, filtering, and CRUD operations |
| Chart.js | Interactive academic charts and visualizations |
| Lucide Icons | Icons for dashboard components and navigation |
| JSON | Portable student record storage and data exchange |
| Browser localStorage | Client-side data and session persistence |
| File API | Importing and exporting JSON files |

---

## Project Structure

```text
student_management_system/
│
├── index.html
│   └── Main dashboard and academic analytics
│
├── login.html
│   └── Login interface
│
├── student_management_system.py
│   └── Python command-line application
│
├── students.json
│   └── Student records in JSON format
│
└── README.md
    └── Project documentation
```

---

## How to Run the Project

### Option 1: VS Code Terminal (PowerShell)

Open the terminal inside `D:\student_management_system` (`Ctrl + ``) and run:

```powershell
start http://127.0.0.1:8000/login.html; python -m http.server 8000 --bind 127.0.0.1
```

### Option 2: Windows Command Prompt (CMD)

Open CMD from anywhere and run:

```cmd
cd /d D:\student_management_system & start http://127.0.0.1:8000/login.html & python -m http.server 8000 --bind 127.0.0.1
```

### Stopping the Server

Press `Ctrl + C` in the terminal when you are done.

---

## Demo Login Credentials

| Username | Password |
|---|---|
| admin | admin123 |
| sara | edumanage |

**Note:** These are demonstration credentials, not production-grade authentication. Do not use real or sensitive passwords.

---

## Student Record Structure

Each student record contains the following fields:

| Field | Description |
|---|---|
| ID | Unique student identifier |
| Name | Student's full name |
| Age | Student's age |
| Branch | Academic department or specialization |
| Marks | Student's academic score (0–100) |

Example JSON record:

```json
{
  "id": 101,
  "name": "Rahul Sharma",
  "age": 20,
  "branch": "CSE",
  "marks": 85
}
```

### Input Validation

The application validates student information using the following rules:

- Student ID must be unique.
- Age must be greater than zero.
- Marks must be between 0 and 100.
- Required student fields must not be empty.

---

## Future Enhancements

Potential improvements for future versions include:

- Integrating a Python Flask or FastAPI backend.
- Replacing JSON-only storage with an SQLite database.
- Implementing secure authentication with password hashing.
- Adding role-based access for administrators and faculty.
- Supporting student attendance management.
- Generating downloadable academic reports.
- Adding automated unit and integration tests.

---

## Learning Outcomes

Through this project, I explored and practiced:

- Building responsive web interfaces.
- Implementing JavaScript-based CRUD operations.
- Working with JSON data and browser storage.
- Creating interactive charts using Chart.js.
- Writing Python command-line applications.
- Running local web applications using Python's HTTP server.
- Organizing and documenting a software project.