def calculate_ats_score(text):

    score = 0

    text = text.lower()


    # Check important resume sections

    sections = [
        "education",
        "experience",
        "skills",
        "projects",
        "summary"
    ]


    for section in sections:

        if section in text:
            score += 10



    # Check contact information

    if "email" in text or "@" in text:
        score += 10


    if "phone" in text or "+" in text:
        score += 10



    # Check action words

    action_words = [
        "managed",
        "developed",
        "created",
        "implemented",
        "led"
    ]


    for word in action_words:

        if word in text:
            score += 5



    # Maximum score = 100

    if score > 100:
        score = 100


    return score