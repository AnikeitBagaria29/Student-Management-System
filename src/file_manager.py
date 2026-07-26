"""
file_manager.py
-------------------------------------
Handles saving and loading student records from a CSV file.

Author : Anikeit Bagaria
Course : Python Programming Laboratory
"""

import csv
import os
from student import Student

# CSV file location
FILE_NAME = "students.csv"


def save_students(students):
    """
    Save all student records to a CSV file.
    """

    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # Header Row
            writer.writerow([
                "Roll No",
                "Name",
                "Age",
                "Department",
                "Python",
                "Data Science",
                "Statistics",
                "Average",
                "Grade"
            ])

            # Student Records
            for student in students:
                writer.writerow(student.to_list())

    except Exception as error:
        print(f"\nError while saving file: {error}\n")


def load_students():
    """
    Load student records from CSV file.

    Returns:
        list of Student objects
    """

    students = []

    # Create empty list if file does not exist
    if not os.path.exists(FILE_NAME):
        return students

    try:

        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:

            reader = csv.reader(file)

            # Skip Header
            next(reader, None)

            for row in reader:
                if len(row) >= 7:
                    student = Student.from_list(row)
                    print(student)
                    students.append(student)

    except FileNotFoundError:
        print("\nStudent database not found.\n")

    except PermissionError:
        print("\nPermission denied while opening file.\n")

    except Exception as error:
        print(f"\nError reading file: {error}\n")

    return students


def backup_file():
    """
    Create a backup of the student database.
    """

    if not os.path.exists(FILE_NAME):
        print("\nNo database available for backup.\n")
        return

    try:

        backup_name = "students_backup.csv"

        with open(FILE_NAME, "r", encoding="utf-8") as source, \
             open(backup_name, "w", newline="", encoding="utf-8") as destination:

            destination.write(source.read())

        print(f"\nBackup created successfully: {backup_name}\n")

    except Exception as error:
        print(f"\nBackup failed: {error}\n")


def clear_database():
    """
    Delete all records from the CSV file.
    """

    try:

        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Roll No",
                "Name",
                "Age",
                "Department",
                "Python",
                "Data Science",
                "Statistics",
                "Average",
                "Grade",
                "GPA"
            ])

        print("\nDatabase cleared successfully.\n")

    except Exception as error:
        print(f"\nError clearing database: {error}\n")