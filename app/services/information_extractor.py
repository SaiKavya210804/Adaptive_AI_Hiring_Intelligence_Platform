import re


KNOWN_SKILLS = [
    "Python",
    "SQL",
    "Machine Learning",
    "TensorFlow",
    "NLP",
    "Power BI",
    "Streamlit",
    "Excel",
    "Tableau",
    "Statistics",
    "Java",
    "HTML",
    "CSS",
    "Git"
]


def extract_name(text):
    """
    Extract candidate name from first line.
    """
    lines = text.strip().split("\n")

    if lines:
        return lines[0].strip()

    return "Unknown"


def extract_email(text):
    """
    Extract email using regex.
    """
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    match = re.search(pattern, text)

    return match.group(0) if match else "Not Found"


def extract_phone(text):
    """
    Extract phone number using regex.
    """
    pattern = r"\+?\d[\d\s\-]{8,15}"

    match = re.search(pattern, text)

    return match.group(0) if match else "Not Found"


def extract_skills(text):
    """
    Extract matching skills from predefined skill list.
    """
    found_skills = []

    text_lower = text.lower()

    for skill in KNOWN_SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def extract_candidate_information(text):

    candidate_data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }

    return candidate_data