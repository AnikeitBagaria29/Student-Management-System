"""
Student Management System
-------------------------
Main Program

Author : Anikeit Bagaria
Course : M. Tech. CSE
"""

from student import Student
from file_manager import save_students, load_students
from analytics import show_statistics, plot_grade_distribution, plot_gpa_distribution
from report_card import generate_report
from dashboard import (
    show_dashboard,
    student_passport,
    show_leaderboard,
    department_statistics,
    grade_distribution,
    scholarship_students,
    academic_insights
)
from reports import (
    generate_report_card,
    export_topper_report,
    export_scholarship_report,
    print_summary
)

students = load_students()

def add_student():
    """Add a new student."""
    try:
        roll = input("Enter Roll Number: ")
        # Check duplicate roll number
        for student in students:
            if student.roll_no == roll:
                print("\nStudent with this Roll Number already exists.\n")
                return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        python = float(input("Python Marks: "))
        ds = float(input("Data Science Marks: "))
        statistics = float(input("Statistics Marks: "))
        new_student = Student(roll, name, age, department, python, ds, statistics)
        students.append(new_student)
        print("\nStudent Added Successfully.\n")
    except ValueError:
        print("\nInvalid Input!\n")

def display_students():
    if len(students) == 0:
        print("\nNo Records Found.\n")
        return
    print("\n========== STUDENT RECORDS ==========\n")
    for student in students:
        student.display()

def search_student():
    roll = input("Enter Roll Number: ")
    for student in students:
        if student.roll_no == roll:
            print()
            student.display()
            return
    print("\nStudent Not Found.\n")

def update_student():
    roll = input("Enter Roll Number to Update: ")
    for student in students:
        if student.roll_no == roll:
            print("\nEnter New Details\n")
            student.name = input("Name: ")
            student.age = int(input("Age: "))
            student.department = input("Department: ")
            student.python = float(input("Python Marks: "))
            student.ds = float(input("Data Science Marks: "))
            student.statistics = float(input("Statistics Marks: "))
            student.calculate_average()
            student.calculate_grade()

            print("\nRecord Updated Successfully.\n")
            return
    print("\nStudent Not Found.\n")

def delete_student():
    roll = input("Enter Roll Number: ")
    for student in students:
        if student.roll_no == roll:
            students.remove(student)
            print("\nRecord Deleted Successfully.\n")
            return
    print("\nStudent Not Found.\n")

def save_records():
    save_students(students)
    print("\nRecords Saved Successfully.\n")

def generate_report_card():
    roll = input("Enter Roll Number : ")
    for student in students:
        if student.roll_no == roll:
            generate_report(student)

def show_menu():
    print("=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Records")
    print("7. Student Statistics")
    print("7. Department Statistics")
    print("8. Grade Distribution")
    print("8. Grade Distribution Chart")
    print("9. GPA Distribution")
    print("10. Generate PDF Report Card")
    print("11. Smart Dashboard")
    print("12. Student Passport")
    print("13. Leaderboard")
    print("13. Academic Insights")
    print("14. Export Topper Report")
    print("15. Scholarship List")
    print("15. Export Scholarship Report")
    print("16. Summary Report")
    print("17. Exit")
    print("=" * 45)

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                display_students()
            elif choice == 3:
                search_student()
            elif choice == 4:
                update_student()
            elif choice == 5:
                delete_student()
            elif choice == 6:
                save_records()
            elif choice == 7:
                show_statistics(students)
            elif choice == 8:
                plot_grade_distribution(students)
            elif choice == 9:
                plot_gpa_distribution(students)
            elif choice == 10:
                generate_report_card()
            elif choice == 11:
                save = input("Do you want to save records before exiting? (Y/N): ")
                if save.upper() == "Y":
                    save_students(students)
                print("\nThank You for Using Student Management System.")
                break
            else:
                print("\nPlease Enter a Valid Choice.\n")
        except ValueError:
            print("\nInvalid Choice! Enter a Number.\n")

if __name__ == "__main__":
    main()