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


def extract_required_skills(job_description):
    """
    Extract required skills from job description text.
    """

    found_skills = []

    jd_lower = job_description.lower()

    for skill in KNOWN_SKILLS:

        # Prevent false matches like:
        # Python matching Pythonic
        pattern = rf"\b{re.escape(skill.lower())}\b"

        if re.search(pattern, jd_lower):
            found_skills.append(skill)

    return found_skills


def parse_job_description(file_path):
    """
    Parse job description text file.
    """

    try:

        with open(file_path, "r", encoding="utf-8") as file:
            jd_text = file.read()

        extracted_data = {
            "required_skills": extract_required_skills(jd_text),
            "raw_text": jd_text
        }

        return extracted_data

    except FileNotFoundError:

        return {
            "error": f"File not found: {file_path}"
        }


if __name__ == "__main__":

    jd_path = "data/job_descriptions/data_scientist_jd.txt"

    result = parse_job_description(jd_path)

    print("\n===== JOB DESCRIPTION PARSED =====\n")

    for key, value in result.items():
        print(f"{key}: {value}")