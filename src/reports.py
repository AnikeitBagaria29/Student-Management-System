"""
reports.py
------------------------------------------
EduVision AI
Smart Student Success & Academic Analytics

Generates:
✓ Individual PDF Report Cards
✓ Topper Report (CSV)
✓ Scholarship Report (CSV)
✓ Summary Report
------------------------------------------
"""

import csv
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ---------------------------------------------------
# PDF REPORT CARD
# ---------------------------------------------------
def generate_report_card(student):

    filename = f"Report_{student.roll_no}.pdf"
    pdf = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph(
        "<font size=20><b>EduVision AI</b></font>",
        styles["Title"]
    )

    subtitle = Paragraph(
        "<b>Student Academic Report Card</b>",
        styles["Heading2"]
    )

    story.append(title)
    story.append(subtitle)
    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Roll Number :</b> {student.roll_no}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Name :</b> {student.name}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Department :</b> {student.department}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Age :</b> {student.age}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    table_data = [
        ["Subject", "Marks"],
        ["Python", student.python],
        ["Data Science", student.ds],
        ["Statistics", student.statistics],
        ["Average", round(student.average, 2)],
        ["Grade", student.grade],
        ["GPA", student.calculate_gpa()]
    ]

    table = Table(table_data)

    table.setStyle(

        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10)
        ])
    )

    story.append(table)
    story.append(Spacer(1, 20))

    if student.calculate_gpa() >= 9:
        remark = "Outstanding Performance"
    elif student.calculate_gpa() >= 8:
       remark = "Excellent Performance"
    elif student.calculate_gpa() >= 7:
        remark = "Very Good"
    elif student.calculate_gpa() >= 6:
        remark = "Good"
    else:
        remark = "Needs Improvement"

    story.append(
        Paragraph(
            f"<b>Teacher Remarks:</b> {remark}",
            styles["Normal"]
        )

    )

    scholarship = "Eligible" if student.calculate_gpa() >= 8.5 else "Not Eligible"

    story.append(
        Paragraph(
            f"<b>Scholarship Status:</b> {scholarship}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 30))

    story.append(
        Paragraph("______________________________", styles["Normal"])
    )

    story.append(
        Paragraph("Class Teacher Signature", styles["Normal"])
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("______________________________", styles["Normal"])
    )

    story.append(
        Paragraph("Principal Signature", styles["Normal"])
    )

    pdf.build(story)
    print(f"{filename} generated successfully.")

# ---------------------------------------------------
# TOPPER REPORT
# ---------------------------------------------------
def export_topper_report(students):
    students = sorted(
        students,
        key=lambda s: s.average,
        reverse=True
    )
    with open(
        "topper_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)
        writer.writerow(["Rank","Roll","Name","Department","Average","Grade","GPA"])
        rank = 1
        for student in students:
            writer.writerow(
                [
                    rank,
                    student.roll_no,
                    student.name,
                    student.department,
                    round(student.average, 2),
                    student.grade,
                    student.calculate_gpa()
                ]
            )
            rank += 1
    print("Topper report exported.")

# ---------------------------------------------------
# SCHOLARSHIP REPORT
# ---------------------------------------------------
def export_scholarship_report(students):

    with open(
        "scholarship_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)
        writer.writerow(["Roll","Name","Department","GPA","Status"])
        for student in students:
            status = (
                "Eligible"
                if student.calculate_gpa() >= 8.5
                else "Not Eligible"
            )
            writer.writerow(
                [
                    student.roll_no,
                    student.name,
                    student.department,
                    student.calculate_gpa(),
                    status
                ]
            )
    print("Scholarship report exported.")

# ---------------------------------------------------
# SUMMARY REPORT
# ---------------------------------------------------
def print_summary(students):
    total = len(students)
    topper = max(students,key=lambda s: s.average)
    avg = sum(s.average for s in students) / total
    print("\n==============================")
    print("EDUVISION AI SUMMARY REPORT")
    print("==============================")
    print("Total Students :", total)
    print("Class Average  :", round(avg, 2))
    print("Top Performer  :", topper.name)
    print("Highest Marks  :", round(topper.average, 2))
    print("==============================")