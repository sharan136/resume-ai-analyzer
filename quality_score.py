def calculate_quality_score(
        resume_score,
        ats_score,
        job_score,
        experience_analysis
):

    # Main scoring weights

    overall = (
        (resume_score * 0.4) +
        (ats_score * 0.3) +
        (job_score * 0.2)
    )


    # Experience bonus

    experience_bonus = 0


    for item in experience_analysis:

        if "✓" in item:
            experience_bonus += 3


    overall += experience_bonus


    if overall > 100:
        overall = 100


    return int(overall)