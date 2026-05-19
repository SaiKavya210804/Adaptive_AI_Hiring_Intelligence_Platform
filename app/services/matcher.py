def calculate_skill_match(candidate_skills, required_skills):
    """
    Compare candidate skills with job description skills.
    """

    # Normalize skills for comparison
    candidate_skills_normalized = [
        skill.lower() for skill in candidate_skills
    ]

    required_skills_normalized = [
        skill.lower() for skill in required_skills
    ]

    matched_skills = []
    missing_skills = []

    # Compare skills
    for index, skill in enumerate(required_skills_normalized):

        if skill in candidate_skills_normalized:
            matched_skills.append(required_skills[index])

        else:
            missing_skills.append(required_skills[index])

    # Calculate match percentage
    match_percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100 if required_skills else 0

    result = {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "explanation": (
            f"Matched {len(matched_skills)} out of "
            f"{len(required_skills)} required skills."
        )
    }

    return result