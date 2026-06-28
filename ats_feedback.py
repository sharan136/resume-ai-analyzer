def generate_ats_feedback(text):

    text = text.lower()

    feedback = []


    # Resume sections

    if "skills" in text:
        feedback.append(
            "✅ Skills section detected"
        )
    else:
        feedback.append(
            "⚠ Add a dedicated Skills section"
        )


    if "experience" in text or "work experience" in text:
        feedback.append(
            "✅ Experience section detected"
        )
    else:
        feedback.append(
            "⚠ Add your work experience"
        )


    if "education" in text:
        feedback.append(
            "✅ Education section detected"
        )
    else:
        feedback.append(
            "⚠ Add your education details"
        )


    # Project section

    if "project" in text:
        feedback.append(
            "✅ Projects section detected"
        )
    else:
        feedback.append(
            "⚠ Add projects to improve ATS ranking"
        )


    # Achievements

    numbers = any(char.isdigit() for char in text)

    if numbers:
        feedback.append(
            "✅ Resume contains measurable results"
        )
    else:
        feedback.append(
            "⚠ Add numbers and achievements (example: improved efficiency by 30%)"
        )


    return feedback