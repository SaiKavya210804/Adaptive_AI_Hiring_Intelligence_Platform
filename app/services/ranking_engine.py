import os

from app.services.resume_parser import extract_resume_text
from app.services.information_extractor import (
    extract_candidate_information
)
from app.services.matcher import calculate_skill_match
from app.services.semantic_matcher import (
    calculate_semantic_similarity
)


def rank_candidates(
    resume_folder,
    required_skills,
    job_description_text
):
    """
    Rank all candidates using:
    - keyword matching
    - semantic similarity
    - hybrid scoring
    """

    candidate_results = []

    for file_name in os.listdir(resume_folder):

        if file_name.endswith(".pdf"):

            resume_path = os.path.join(
                resume_folder,
                file_name
            )

            try:

                # Extract resume text
                resume_result = extract_resume_text(
                    resume_path
                )

                if not resume_result:
                    continue

                # Extract candidate information
                candidate_info = (
                    extract_candidate_information(
                        resume_result["text"]
                    )
                )

                # Keyword matching
                match_result = calculate_skill_match(
                    candidate_info["skills"],
                    required_skills
                )

                # Semantic similarity
                semantic_result = (
                    calculate_semantic_similarity(
                        resume_result["text"],
                        job_description_text
                    )
                )

                keyword_score = match_result[
                    "match_percentage"
                ]

                semantic_score = semantic_result[
                    "semantic_similarity_score"
                ]

                # Hybrid score
                hybrid_score = round(
                    (
                        0.4 * keyword_score
                        +
                        0.6 * semantic_score
                    ),
                    2
                )

                candidate_data = {
                    "candidate_name":
                    candidate_info["name"],

                    "skills":
                    candidate_info["skills"],

                    "keyword_match_score":
                    keyword_score,

                    "semantic_similarity_score":
                    semantic_score,

                    "hybrid_score":
                    hybrid_score,

                    "matched_skills":
                    match_result["matched_skills"],

                    "missing_skills":
                    match_result["missing_skills"],

                    "explanation":
                    match_result["explanation"]
                }

                candidate_results.append(
                    candidate_data
                )

            except Exception as error:

                print(
                    f"Error processing resume "
                    f"{file_name}: {error}"
                )

    # Sort candidates using hybrid score
    ranked_candidates = sorted(
        candidate_results,
        key=lambda x: x["hybrid_score"],
        reverse=True
    )

    return ranked_candidates