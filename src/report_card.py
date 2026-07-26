from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(student):

    file_name = f"Report_{student.roll_no}.pdf"
    pdf = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()
    elements = []
    title = Paragraph("<b><font size=18>EDUVISION AI REPORT CARD</font></b>",styles["Title"])

    elements.append(title)
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f"<b>Name:</b> {student.name}",styles["Normal"]))
    elements.append(Paragraph(f"<b>Roll Number:</b> {student.roll_no}",styles["Normal"]))
    elements.append(Paragraph(f"<b>Department:</b> {student.department}",styles["Normal"]))
    elements.append(Spacer(1, 20))

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
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10)
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<b>Teacher Remarks:</b> Excellent Performance",styles["Normal"]))
    elements.append(Paragraph("<b>Scholarship:</b> Eligible",styles["Normal"]))
    pdf.build(elements)
    print(file_name, "created successfully.")