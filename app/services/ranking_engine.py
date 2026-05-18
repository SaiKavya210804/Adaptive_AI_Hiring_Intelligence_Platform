import os

from app.services.resume_parser import extract_resume_text
from app.services.information_extractor import extract_candidate_information
from app.services.matcher import calculate_skill_match


def rank_candidates(resume_folder, required_skills):

    candidate_results = []

    for file_name in os.listdir(resume_folder):

        if file_name.endswith(".pdf"):

            resume_path = os.path.join(resume_folder, file_name)

            # Extract resume text
            resume_result = extract_resume_text(resume_path)

            if not resume_result:
                continue

            # Extract candidate info
            candidate_info = extract_candidate_information(
                resume_result["text"]
            )

            # Calculate match
            match_result = calculate_skill_match(
                candidate_info["skills"],
                required_skills
            )

            candidate_data = {
                "candidate_name": candidate_info["name"],
                "skills": candidate_info["skills"],
                "match_percentage": match_result["match_percentage"],
                "matched_skills": match_result["matched_skills"],
                "missing_skills": match_result["missing_skills"]
            }

            candidate_results.append(candidate_data)

    # Sort highest score first
    ranked_candidates = sorted(
        candidate_results,
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return ranked_candidates