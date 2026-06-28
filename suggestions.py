suggestion_map = {

    "risk management":
    "Add examples where you identified risks and created mitigation plans.",

    "leadership":
    "Mention team handling, mentoring, or leadership responsibilities.",

    "git":
    "Add GitHub projects and version control experience.",

    "sql":
    "Include database projects and SQL queries.",

    "python":
    "Add Python projects with real-world applications.",

    "communication":
    "Mention client interaction and stakeholder communication examples.",

    "budget management":
    "Add examples of handling project budgets and cost optimization."

}


def get_suggestions(missing):

    suggestions = []

    for skill in missing:

        skill_lower = skill.lower()

        if skill_lower in suggestion_map:
            suggestions.append(
                suggestion_map[skill_lower]
            )

    return suggestions