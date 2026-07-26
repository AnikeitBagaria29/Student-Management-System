"""
student.py
------------------------------
Student Class for Student Management System
Author : Anikeit Bagaria
Course : Python Programming Laboratory
"""

class Student:
    """Represents a student and related operations."""

    def __init__(self, roll_no, name, age, department,
                 python, ds, statistics):

        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.department = department

        self.python = python
        self.ds = ds
        self.statistics = statistics

        self.average = 0
        self.grade = ""

        self.calculate_average()
        self.calculate_grade()

    def calculate_average(self):
        """Calculate average marks."""
        self.average = (
            self.python +
            self.ds +
            self.statistics
        ) / 3

    def calculate_grade(self):
        """Assign grade based on average."""
        if self.average >= 90:
            self.grade = "A+"
        elif self.average >= 80:
            self.grade = "A"
        elif self.average >= 70:
            self.grade = "B"
        elif self.average >= 60:
            self.grade = "C"
        elif self.average >= 50:
            self.grade = "D"
        else:
            self.grade = "Fail"

    def display(self):
        """Display student details."""
        print("-" * 45)
        print(f"Roll Number : {self.roll_no}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Department  : {self.department}")
        print(f"Python      : {self.python}")
        print(f"Data Science: {self.ds}")
        print(f"Statistics  : {self.statistics}")
        print(f"Average     : {self.average:.2f}")
        print(f"Grade       : {self.grade}")
        print(f"GPA         : {self.calculate_gpa():.1f}")
        print("-" * 45)

    def calculate_gpa(self):
        """Calculate GPA on a 10-point scale."""
        if self.average >= 90:
            return 10.0
        elif self.average >= 80:
            return 9.0
        elif self.average >= 70:
            return 8.0
        elif self.average >= 60:
            return 7.0
        elif self.average >= 50:
            return 6.0
        elif self.average >= 40:
            return 5.0
        else:
            return 0.0
    
    def to_list(self):
        """Convert object into list. Used while writing CSV files."""
        return [
            self.roll_no,
            self.name,
            self.age,
            self.department,
            self.python,
            self.ds,
            self.statistics,
            round(self.average, 2),
            self.grade,
            self.calculate_gpa()
        ]

    @classmethod
    def from_list(cls, data):
        """Create Student object from CSV row."""
        return cls(
            data[0],
            data[1],
            int(data[2]),
            data[3],
            float(data[4]),
            float(data[5]),
            float(data[6])
        )

    def __str__(self):
        """Return string representation."""
        return (
            f"{self.roll_no} | "
            f"{self.name} | "
            f"{self.department} | "
            f"{self.average:.2f} | "
            f"{self.grade}"
        )