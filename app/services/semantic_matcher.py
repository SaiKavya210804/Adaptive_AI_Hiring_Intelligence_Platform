from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_semantic_similarity(
    resume_text,
    job_description_text
):
    """
    Calculate semantic similarity between
    resume text and job description text.
    """

    # Generate embeddings together
    embeddings = model.encode([
        resume_text,
        job_description_text
    ])

    resume_embedding = [embeddings[0]]
    jd_embedding = [embeddings[1]]

    # Calculate cosine similarity
    similarity_score = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]

    # Convert to percentage
    similarity_percentage = round(
        float(similarity_score) * 100,
        2
    )

    return {
        "semantic_similarity_score":
        similarity_percentage
    }


if __name__ == "__main__":

    sample_resume = """
    Experienced Python developer with
    machine learning and NLP experience.
    """

    sample_jd = """
    Looking for a Data Scientist skilled in
    Python, NLP, and machine learning.
    """

    result = calculate_semantic_similarity(
        sample_resume,
        sample_jd
    )

    print("\n===== SEMANTIC MATCH RESULT =====\n")

    print(
        f"Semantic Similarity Score: "
        f"{result['semantic_similarity_score']}%"
    )