"""
analytics.py
--------------------------------------
Student Data Analysis and Visualization
Author : Anikeit Bagaria
Course : M. Tech CSE
"""

import pandas as pd
import matplotlib.pyplot as plt

def show_statistics(students):
    """Display summary statistics of student records."""

    if not students:
        print("\nNo student records available.\n")
        return

    data = []

    for student in students:
        data.append({
            "Roll No": student.roll_no,
            "Name": student.name,
            "Department": student.department,
            "Python": student.python,
            "Data Science": student.ds,
            "Statistics": student.statistics,
            "Average": student.average,
            "Grade": student.grade,
            "GPA": student.calculate_gpa()
        })

    df = pd.DataFrame(data)

    print("\n" + "=" * 50)
    print("         STUDENT STATISTICS")
    print("=" * 50)

    print(f"Total Students        : {len(df)}")
    print(f"Highest Average       : {df['Average'].max():.2f}")
    print(f"Lowest Average        : {df['Average'].min():.2f}")
    print(f"Class Average         : {df['Average'].mean():.2f}")
    print(f"Highest Average       : {df['GPA'].max():.2f}")
    print(f"Lowest Average        : {df['GPA'].min():.2f}")
    print(f"Average GPA           : {df['GPA'].mean():.2}")

    topper = df.loc[df["Average"].idxmax()]

    print("\nTop Performer")
    print("--------------------------")
    print(f"Name    : {topper['Name']}")
    print(f"Average : {topper['Average']:.2f}")
    print(f"Grade   : {topper['Grade']}")

    print("\nDepartment-wise Average")
    print("--------------------------")
    print(df.groupby("Department")["Average"].mean().round(2))

    print("\nGrade Distribution")
    print("--------------------------")
    print(df["Grade"].value_counts())

    print("=" * 50)


def plot_grade_distribution(students):
    """isplay grade distribution using a pie chart."""

    if not students:
        print("\nNo student records available.\n")
        return

    grades = {}

    for student in students:

        if student.grade in grades:
            grades[student.grade] += 1
        else:
            grades[student.grade] = 1

    plt.figure(figsize=(7, 7))

    plt.pie(
        grades.values(),
        labels=grades.keys(),
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Grade Distribution")
    plt.axis("equal")

    plt.show()

def plot_gpa_distribution(students):

    if not students:
        print("No Records Found")
        return

    import matplotlib.pyplot as plt

    gpas = [student.calculate_gpa() for student in students]

    plt.figure(figsize=(8,5))

    plt.hist(gpas, bins=6)

    plt.title("GPA Distribution")
    plt.xlabel("GPA")
    plt.ylabel("Number of Students")

    plt.grid(True)

    plt.show()

def plot_student_average(students):
    """Display average marks of each student using a bar chart."""

    if not students:
        print("\nNo student records available.\n")
        return

    names = [student.name for student in students]
    averages = [student.average for student in students]

    plt.figure(figsize=(10, 5))

    plt.bar(names, averages)

    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("Student-wise Average Marks")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

def plot_subject_comparison(students):
    """Compare subject-wise average marks."""

    if not students:
        print("\nNo student records available.\n")
        return

    python_avg = sum(student.python for student in students) / len(students)
    ds_avg = sum(student.ds for student in students) / len(students)
    statistics_avg = sum(student.statistics for student in students) / len(students)

    subjects = [
        "Python",
        "Data Science",
        "Statistics"
    ]

    averages = [
        python_avg,
        ds_avg,
        statistics_avg
    ]

    plt.figure(figsize=(6, 5))

    plt.bar(subjects, averages)

    plt.title("Subject-wise Average Marks")
    plt.ylabel("Average Marks")

    plt.tight_layout()

    plt.show()

def export_statistics(students):
    """Export student statistics to a CSV file."""

    if not students:
        print("\nNo student records available.\n")
        return

    data = []

    for student in students:
        data.append({
            "Roll No": student.roll_no,
            "Name": student.name,
            "Department": student.department,
            "Average": round(student.average, 2),
            "Grade": student.grade
        })

    df = pd.DataFrame(data)

    df.to_csv("student_statistics.csv", index=False)

    print("\nStatistics exported to student_statistics.csv\n")