def analyze_experience(text):

    text_lower = text.lower()

    result = []


    # Experience level

    if any(word in text_lower for word in [
        "10 years",
        "8 years",
        "7 years",
        "senior"
    ]):

        result.append(
            "Experience Level: Senior"
        )


    elif any(word in text_lower for word in [
        "3 years",
        "4 years",
        "5 years",
        "intermediate"
    ]):

        result.append(
            "Experience Level: Intermediate"
        )


    elif any(word in text_lower for word in [
        "intern",
        "fresher",
        "student",
        "0 years",
        "1 year"
    ]):

        result.append(
            "Experience Level: Entry Level"
        )


    else:

        result.append(
            "Experience Level: Not Detected"
        )



    # Leadership detection

    leadership_words = [
        "managed",
        "led",
        "supervised",
        "coordinated",
        "team",
        "stakeholder"
    ]


    leadership_found = False


    for word in leadership_words:

        if word in text_lower:
            leadership_found = True



    if leadership_found:

        result.append(
            "✓ Leadership experience detected"
        )

    else:

        result.append(
            "⚠ Add leadership examples"
        )



    # Achievement detection

    has_numbers = any(
        char.isdigit()
        for char in text
    )


    if has_numbers:

        result.append(
            "✓ Resume contains measurable achievements"
        )

    else:

        result.append(
            "⚠ Add measurable results (example: improved efficiency by 30%)"
        )



    # Action verbs

    action_words = [
        "developed",
        "implemented",
        "created",
        "managed",
        "improved",
        "optimized"
    ]


    action_found = False


    for word in action_words:

        if word in text_lower:
            action_found = True



    if action_found:

        result.append(
            "✓ Good use of action verbs"
        )

    else:

        result.append(
            "⚠ Add stronger action verbs"
        )


    return result