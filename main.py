from app.services.job_description_parser import parse_job_description
from app.services.ranking_engine import rank_candidates


# Resume folder
resume_folder = "data/resumes"

# JD path
jd_path = "data/job_descriptions/data_scientist_jd.txt"


# Parse JD
jd_result = parse_job_description(jd_path)


# Rank all candidates
ranked_candidates = rank_candidates(
    resume_folder,
    jd_result["required_skills"]
)


print("\n===== CANDIDATE RANKINGS =====\n")


for index, candidate in enumerate(ranked_candidates, start=1):

    print(f"Rank #{index}")

    print(f"Candidate: {candidate['candidate_name']}")

    print(f"Match Percentage: {candidate['match_percentage']}%")

    print(f"Matched Skills: {candidate['matched_skills']}")

    print(f"Missing Skills: {candidate['missing_skills']}")

    print("-" * 50)