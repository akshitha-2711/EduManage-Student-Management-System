
"""
Student Management System
Beginner-friendly Python project.
Student records are saved in students.json.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


# Load student records from the file
def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not load student records.")
        return []


# Save student records to the file
def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


# Find a student using student ID
def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


# Add a new student
def add_student(students):
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(students, student_id):
        print("Student ID already exists.")
        return

    name = input("Enter Name: ").strip()
    age_text = input("Enter Age: ").strip()
    branch = input("Enter Branch: ").strip()
    marks_text = input("Enter Marks (0-100): ").strip()

    if not name or not branch:
        print("Name and branch cannot be empty.")
        return

    try:
        age = int(age_text)
        marks = float(marks_text)

        if age <= 0 or not 0 <= marks <= 100:
            raise ValueError

    except ValueError:
        print("Please enter a valid age and marks between 0 and 100.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "branch": branch,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# View all students
def view_students(students):
    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])


# Search for a student
def search_student(students):
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ").strip()
    student = find_student(students, student_id)

    if student:
        print("\nStudent Found!")
        for key, value in student.items():
            print(key.title() + ":", value)
    else:
        print("Student not found.")


# Update student information
def update_student(students):
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")

    name = input(f'New Name [{student["name"]}]: ').strip()
    age_text = input(f'New Age [{student["age"]}]: ').strip()
    branch = input(f'New Branch [{student["branch"]}]: ').strip()
    marks_text = input(f'New Marks [{student["marks"]}]: ').strip()

    if name:
        student["name"] = name

    if branch:
        student["branch"] = branch

    try:
        if age_text:
            age = int(age_text)
            if age <= 0:
                raise ValueError
            student["age"] = age

        if marks_text:
            marks = float(marks_text)
            if not 0 <= marks <= 100:
                raise ValueError
            student["marks"] = marks

    except ValueError:
        print("Invalid age or marks. Please check your input.")
        return

    save_students(students)
    print("Student updated successfully!")


# Delete a student
def delete_student(students):
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ").strip()
    student = find_student(students, student_id)

    if student:
        students.remove(student)
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main menu
def main():
    students = load_students()

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


# Start the program
if __name__ == "__main__":
    main()
