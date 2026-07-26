"""
dashboard.py
--------------------------------------------------
EduVision AI
Smart Student Success & Academic Analytics System
Dashboard Module
--------------------------------------------------
"""

from collections import Counter
from statistics import mean

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------
def show_dashboard(students):
    if not students:
        print("\nNo student records available.")
        return

    total_students = len(students)
    class_average = mean(student.average for student in students)
    average_gpa = mean(student.calculate_gpa() for student in students)
    topper = max(students, key=lambda s: s.average)
    passed = len([s for s in students if s.grade != "F"])
    pass_percentage = (passed / total_students) * 100
    scholarship = len(
        [
            s for s in students
            if s.calculate_gpa() >= 8.5
        ]
    )

    needs_support = len(
        [
            s for s in students
            if s.calculate_gpa() < 6
        ]
    )

    print("\n" + "=" * 65)
    print("          EDUVISION AI - SMART DASHBOARD")
    print("=" * 65)
    print(f"👨‍🎓 Total Students        : {total_students}")
    print(f"📈 Class Average         : {class_average:.2f}")
    print(f"🎓 Average GPA           : {average_gpa:.2f}")
    print(f"🏆 Top Performer         : {topper.name}")
    print(f"⭐ Highest Average       : {topper.average:.2f}")
    print(f"✅ Pass Percentage       : {pass_percentage:.2f}%")
    print(f"🎯 Scholarship Eligible  : {scholarship}")
    print(f"⚠ Needs Support         : {needs_support}")
    print("=" * 65)

# --------------------------------------------------
# LEADERBOARD
# --------------------------------------------------
def show_leaderboard(students, top=10):
    print("\nTOP PERFORMERS")
    print("-" * 65)

    sorted_students = sorted(
        students,
        key=lambda s: s.average,
        reverse=True
    )

    print(
        "{:<5}{:<20}{:<12}{:<10}{:<8}".format(
            "Rank",
            "Name",
            "Department",
            "Average",
            "GPA"
        )
    )

    print("-" * 65)

    for rank, student in enumerate(sorted_students[:top], start=1):

        print(
            "{:<5}{:<20}{:<12}{:<10.2f}{:<8}".format(
                rank,
                student.name,
                student.department,
                student.average,
                student.calculate_gpa()
            )
        )

# --------------------------------------------------
# DEPARTMENT ANALYSIS
# --------------------------------------------------
def department_statistics(students):
    print("\nDEPARTMENT STATISTICS")
    print("-" * 50)
    departments = {}
    for student in students:
        departments.setdefault(
            student.department,
            []
        ).append(student.average)
    print("{:<15}{:<10}{:<15}".format("Department","Students","Average"))
    print("-" * 50)
    for dept, marks in departments.items():
        print("{:<15}{:<10}{:<15.2f}".format(dept,len(marks),mean(marks)))

# --------------------------------------------------
# GRADE DISTRIBUTION
# --------------------------------------------------
def grade_distribution(students):
    grades = Counter(
        student.grade for student in students
    )
    print("\nGRADE DISTRIBUTION")
    print("-" * 40)
    for grade, count in grades.items():
        print(f"{grade:>3} : {'█'*count} ({count})")

# --------------------------------------------------
# SCHOLARSHIP LIST
# --------------------------------------------------
def scholarship_students(students):
    print("\nSCHOLARSHIP ELIGIBLE STUDENTS")
    print("-" * 60)
    eligible = sorted(
        [
            s for s in students
            if s.calculate_gpa() >= 8.5
        ],
        key=lambda x: x.average,
        reverse=True
    )

    if not eligible:
        print("No eligible students.")
        return
    print("{:<10}{:<20}{:<12}{:<8}".format("Roll","Name","Department","GPA"))
    print("-" * 60)

    for student in eligible:
        print(
            "{:<10}{:<20}{:<12}{:<8}".format(
                student.roll_no,
                student.name,
                student.department,
                student.calculate_gpa()
            )
        )

# --------------------------------------------------
# ACADEMIC INSIGHTS
# --------------------------------------------------
def academic_insights(students):
    topper = max(students, key=lambda s: s.average)
    lowest = min(students, key=lambda s: s.average)
    print("\nACADEMIC INSIGHTS")
    print("-" * 60)
    print(f"🏆 Top Performer      : {topper.name}")
    print(f"📈 Highest Average    : {topper.average:.2f}")
    print(f"📉 Lowest Performer   : {lowest.name}")
    print(f"📊 Lowest Average     : {lowest.average:.2f}")
    print(f"🎓 Average GPA        : {mean(s.calculate_gpa() for s in students):.2f}")
    print(f"👨‍🎓 Total Students    : {len(students)}")
    print("-" * 60)

# --------------------------------------------------
# STUDENT PASSPORT
# --------------------------------------------------
def student_passport(student):
    print("\n" + "=" * 60)
    print("             STUDENT ACADEMIC PASSPORT")
    print("=" * 60)
    print(f"Roll Number     : {student.roll_no}")
    print(f"Name            : {student.name}")
    print(f"Department      : {student.department}")
    print(f"Age             : {student.age}")
    print("-" * 60)
    print(f"Python          : {student.python}")
    print(f"Data Science    : {student.ds}")
    print(f"Statistics      : {student.statistics}")
    print("-" * 60)
    print(f"Average Marks   : {student.average:.2f}")
    print(f"Grade           : {student.grade}")
    print(f"GPA             : {student.calculate_gpa()}")
    print("=" * 60)