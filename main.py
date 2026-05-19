from app.services.job_description_parser import (
    parse_job_description
)
from app.services.ranking_engine import (
    rank_candidates
)


# Resume folder
resume_folder = "data/resumes"

# Job description path
jd_path = (
    "data/job_descriptions/data_scientist_jd.txt"
)


# Parse job description
jd_result = parse_job_description(jd_path)


# Handle missing JD file
if "error" in jd_result:

    print(f"\nError: {jd_result['error']}")

    exit()


# Rank candidates
ranked_candidates = rank_candidates(
    resume_folder,
    jd_result["required_skills"],
    jd_result["raw_text"]
)


# Handle empty rankings
if not ranked_candidates:

    print(
        "\nNo candidates found or "
        "no resumes could be processed."
    )

    exit()


print("\n===== CANDIDATE RANKINGS =====\n")


for index, candidate in enumerate(
    ranked_candidates,
    start=1
):

    print(f"Rank #{index}")

    print(
        f"Candidate: "
        f"{candidate['candidate_name']}"
    )

    print(
        f"Keyword Match Score: "
        f"{candidate['keyword_match_score']}%"
    )

    print(
        f"Semantic Similarity Score: "
        f"{candidate['semantic_similarity_score']}%"
    )

    print(
        f"Hybrid Score: "
        f"{candidate['hybrid_score']}%"
    )

    print(
        f"Matched Skills: "
        f"{candidate['matched_skills']}"
    )

    print(
        f"Missing Skills: "
        f"{candidate['missing_skills']}"
    )

    print(
        f"Explanation: "
        f"{candidate['explanation']}"
    )

    print("-" * 50)