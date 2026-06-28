from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf(
    filename,
    quality_score,
    score,
    ats_score,
    job_score,
    strengths,
    weaknesses,
    suggestions
):

    pdf = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    y = height - 50


    pdf.setFont("Helvetica-Bold", 20)

    pdf.drawString(
        50,
        y,
        "ResumeAI Analysis Report"
    )


    y -= 40


    pdf.setFont(
        "Helvetica",
        12
    )


    data = [

        f"Overall Resume Quality: {quality_score}%",

        f"Resume Match: {score}%",

        f"ATS Compatibility: {ats_score}%",

        f"Job Match: {job_score}%",

        "",

        "Resume Strengths:"
    ]


    for item in data:

        pdf.drawString(
            50,
            y,
            item
        )

        y -= 20



    for item in strengths:

        pdf.drawString(
            70,
            y,
            "✓ " + item
        )

        y -= 18



    y -= 20


    pdf.drawString(
        50,
        y,
        "Areas To Improve:"
    )

    y -= 20



    for item in weaknesses:

        pdf.drawString(
            70,
            y,
            item
        )

        y -= 18



    y -= 20


    pdf.drawString(
        50,
        y,
        "AI Suggestions:"
    )

    y -= 20



    for item in suggestions:

        pdf.drawString(
            70,
            y,
            item
        )

        y -= 18



    pdf.save()