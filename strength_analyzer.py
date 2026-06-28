def generate_strengths(
        found,
        missing,
        ats_feedback,
        experience_analysis,
        job_score
):

    strengths = []

    weaknesses = []



    # Skills analysis

    if len(found) >= 5:

        strengths.append(
            "✓ Strong skill alignment with the selected role"
        )

    else:

        weaknesses.append(
            "⚠ Add more role-specific skills"
        )



    # Missing skills

    if len(missing) > 0:

        weaknesses.append(
            "⚠ Improve missing skill coverage"
        )

    else:

        strengths.append(
            "✓ Good keyword coverage"
        )



    # ATS analysis

    for item in ats_feedback:

        if item.startswith("✓"):

            strengths.append(item)

        elif item.startswith("⚠"):

            weaknesses.append(item)



    # Experience

    for item in experience_analysis:

        if "✓" in item:

            strengths.append(item)



    # Job match

    if job_score >= 70:

        strengths.append(
            "✓ Resume matches the job description well"
        )

    else:

        weaknesses.append(
            "⚠ Add more keywords from the job description"
        )



    return strengths, weaknesses