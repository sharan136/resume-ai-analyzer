# analyzer.py


import re

from skills_database import SKILLS_DATABASE
from skill_synonyms import SKILL_SYNONYMS



def clean_text(text):

    """
    Convert resume text into a standard format
    """

    text = text.lower()

    # remove special characters

    text = re.sub(
        r'[^a-z0-9+#.\s]',
        ' ',
        text
    )


    # remove extra spaces

    text = re.sub(
        r'\s+',
        ' ',
        text
    )


    return text





def find_skill_match(resume_text, skill):

    """
    Check whether a skill or its synonyms
    exist in resume
    """


    # Get synonyms

    synonyms = SKILL_SYNONYMS.get(
        skill,
        [
            skill.lower()
        ]
    )


    for word in synonyms:


        word = word.lower()


        if word in resume_text:

            return True



    return False





def analyze_resume(resume_text, role):


    """
    Main resume analyzer

    Returns:
    matched skills
    missing skills
    percentage score

    """



    # clean resume

    resume_text = clean_text(
        resume_text
    )



    # check role exists

    if role not in SKILLS_DATABASE:


        return [], [], 0




    # required skills

    required_skills = SKILLS_DATABASE[role]



    matched = []

    missing = []




    for skill in required_skills:


        if find_skill_match(
            resume_text,
            skill
        ):


            matched.append(skill)


        else:

            missing.append(skill)




    # calculate score


    if len(required_skills) > 0:


        score = int(
            (
                len(matched)
                /
                len(required_skills)
            )
            *
            100
        )


    else:

        score = 0




    return (
        matched,
        missing,
        score
    )