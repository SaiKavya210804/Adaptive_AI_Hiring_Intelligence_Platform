# ---------------------------------------------------
# PATH & WARNINGS CONFIG
# ---------------------------------------------------

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

# ---------------------------------------------------
# THIRD-PARTY LIBRARIES
# ---------------------------------------------------

import streamlit as st
import pandas as pd

# ---------------------------------------------------
# STANDARD LIBRARIES
# ---------------------------------------------------

import os
import tempfile

# ---------------------------------------------------
# LOCAL PROJECT IMPORTS
# ---------------------------------------------------

from app.services.ranking_engine import rank_candidates
from app.services.job_description_parser import extract_required_skills

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Adaptive AI Hiring Intelligence Platform",
    layout="wide"
)

st.title("Adaptive AI Hiring Intelligence Platform")
st.markdown("AI-Powered Resume Screening and Candidate Ranking System")

# ---------------------------------------------------
# SIDEBAR NAVIGATION (FIXED - SINGLE SOURCE OF TRUTH)
# ---------------------------------------------------

pages = [
    "Upload Resumes",
    "Job Description",
    "Candidate Rankings",
    "Analytics"
]

if "current_page" not in st.session_state:
    st.session_state.current_page = pages[0]

st.sidebar.header("Navigation")

selected_page = st.sidebar.radio(
    "Go To",
    pages,
    index=pages.index(st.session_state.current_page)
)

# sync state ONLY when user changes sidebar
if selected_page != st.session_state.current_page:
    st.session_state.current_page = selected_page

page = st.session_state.current_page


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "uploaded_resumes" not in st.session_state:
    st.session_state.uploaded_resumes = []

if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "ranking_results" not in st.session_state:
    st.session_state.ranking_results = []

# ---------------------------------------------------
# PAGE 1 — RESUME UPLOAD
# ---------------------------------------------------

if page == "Upload Resumes":

    st.header("Upload Candidate Resumes")

    os.makedirs("temp_uploads", exist_ok=True)

    uploaded_files = st.file_uploader(
        "Upload PDF Resumes",
        type=["pdf"],
        accept_multiple_files=True,
        key="upload_resumes"
    )

    if uploaded_files:

        saved_files = []

        for file in uploaded_files:
            file_path = os.path.join("temp_uploads", file.name)

            with open(file_path, "wb") as f:
                f.write(file.getbuffer())

            saved_files.append(file.name)

        st.session_state.uploaded_resumes = saved_files
        st.success(f"{len(saved_files)} resumes uploaded successfully.")

    if st.session_state.uploaded_resumes:

        st.subheader("Uploaded Files")

        for file_name in st.session_state.uploaded_resumes:
            st.write(f"📄 {file_name}")

    if st.button("Next → Job Description", key="btn_next_upload"):
        st.session_state.current_page = "Job Description"
        st.rerun()

# ---------------------------------------------------
# PAGE 2 — JOB DESCRIPTION
# ---------------------------------------------------

elif page == "Job Description":

    st.header("Job Description Input")

    jd_text = st.text_area(
        "Paste Job Description Here",
        value=st.session_state.job_description,
        height=300,
        key="jd_input"
    )

    if st.button("Save Job Description", key="btn_save_jd"):
        st.session_state.job_description = jd_text
        st.success("Job Description Saved Successfully")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Previous", key="btn_prev_jd"):
            st.session_state.current_page = "Upload Resumes"
            st.rerun()

    with col2:
        if st.button("Next → Rankings", key="btn_next_jd"):
            st.session_state.current_page = "Candidate Rankings"
            st.rerun()
            
# ---------------------------------------------------
# PAGE 3 — CANDIDATE RANKINGS
# ---------------------------------------------------

elif page == "Candidate Rankings":

    st.header("Candidate Ranking Results")

    if len(st.session_state.uploaded_resumes) == 0:
        st.warning("Please upload resumes first.")

    elif st.session_state.job_description == "":
        st.warning("Please enter a job description first.")

    else:

        required_skills = extract_required_skills(
            st.session_state.job_description
        )

        st.subheader("Extracted Required Skills")
        st.write(required_skills)

        with st.spinner("Running AI Candidate Ranking Engine..."):

            ranked_candidates = rank_candidates(
                resume_folder="temp_uploads",
                required_skills=required_skills,
                job_description_text=st.session_state.job_description
            )

        st.session_state.ranking_results = ranked_candidates

        if not ranked_candidates:
            st.error("No candidates could be ranked.")

        else:

            st.success(f"{len(ranked_candidates)} candidates ranked successfully.")

            ranking_table = []

            for candidate in ranked_candidates:
                ranking_table.append({
                    "Candidate": candidate["candidate_name"],
                    "Keyword Score": candidate["keyword_match_score"],
                    "Semantic Score": candidate["semantic_similarity_score"],
                    "Hybrid Score": candidate["hybrid_score"]
                })

            df = pd.DataFrame(ranking_table)
            df = df.sort_values(by="Hybrid Score", ascending=False)

            st.dataframe(df, use_container_width=True)

            st.subheader("Candidate Insights")

            for candidate in ranked_candidates:

                with st.expander(candidate["candidate_name"]):

                    st.write("Keyword Score:", candidate["keyword_match_score"])
                    st.write("Semantic Score:", candidate["semantic_similarity_score"])
                    st.write("Hybrid Score:", candidate["hybrid_score"])

                    st.write("Matched Skills:")
                    st.write(candidate["matched_skills"])

                    st.write("Missing Skills:")
                    st.write(candidate["missing_skills"])

                    st.write("Explanation:")
                    st.write(candidate["explanation"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("← Previous", key="btn_prev_rank"):
                st.session_state.current_page = "Job Description"
                st.rerun()

        with col2:
            if st.button("Next → Analytics", key="btn_next_rank"):
                st.session_state.current_page = "Analytics"
                st.rerun()

# ---------------------------------------------------
# PAGE 4 — ANALYTICS
# ---------------------------------------------------

# elif page == "Analytics":

#     st.header("Recruitment Analytics Dashboard")

#     st.info("Analytics visualizations will appear here.")

#     analytics_data = {
#         "Metric": [
#             "Total Resumes",
#             "Average Match Score",
#             "Top Candidate Score"
#         ],
#         "Value": [
#             25,
#             "78%",
#             "92%"
#         ]
#     }

#     analytics_df = pd.DataFrame(analytics_data)

#     st.table(analytics_df)

elif page == "Analytics":

    st.header("Recruitment Analytics Dashboard")

    results = st.session_state.get("ranking_results", [])

    if not results:
        st.warning("No ranking data found. Please run Candidate Rankings first.")

    else:

        # -------------------------
        # REAL METRICS
        # -------------------------

        total_resumes = len(results)

        avg_score = sum(r["hybrid_score"] for r in results) / total_resumes

        top_score = max(r["hybrid_score"] for r in results)

        analytics_data = {
            "Metric": [
                "Total Resumes",
                "Average Hybrid Score",
                "Top Candidate Score"
            ],
            "Value": [
                total_resumes,
                f"{avg_score:.2f}",
                f"{top_score:.2f}"
            ]
        }

        analytics_df = pd.DataFrame(analytics_data)

        st.table(analytics_df)

        # -------------------------
        # OPTIONAL: TOP CANDIDATE VIEW
        # -------------------------

        top_candidate = max(results, key=lambda x: x["hybrid_score"])

        st.subheader("Top Candidate Snapshot")

        st.write("Name:", top_candidate["candidate_name"])
        st.write("Hybrid Score:", top_candidate["hybrid_score"])
        st.write("Matched Skills:", top_candidate["matched_skills"])
        st.write("Missing Skills:", top_candidate["missing_skills"])
        st.write("Explanation:", top_candidate["explanation"])

    # -------------------------
    # NAVIGATION BUTTONS
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Previous", key="btn_prev_analytics"):
            st.session_state.current_page = "Candidate Rankings"
            st.rerun()