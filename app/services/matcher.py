def calculate_skill_match(candidate_skills, required_skills):
    """
    Compare candidate skills with JD skills.
    """

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in candidate_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100 if required_skills else 0

    result = {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }

    return result