# Adaptive AI Hiring Intelligence Platform

An AI-assisted hiring analytics platform that helps recruiters parse resumes, compare candidates against job descriptions, rank applicants transparently, and provide explainable hiring insights.

The project focuses on building a modular and scalable hiring intelligence pipeline using Python and NLP techniques.

---

# 🚀 Current Features

## ✅ Resume Parsing
- Extract text from PDF resumes
- Clean and preprocess resume content
- Preserve readable structure

## ✅ Candidate Information Extraction
Extract:
- Candidate name
- Email
- Phone number
- Skills

## ✅ Job Description Parsing
- Parse job descriptions from text files
- Extract required technical skills
- Prepare structured hiring requirements

## ✅ Candidate Matching Engine
- Compare candidate skills with job requirements
- Identify matched skills
- Identify missing skills
- Generate match percentage

## ✅ Automated Candidate Ranking
- Process multiple resumes automatically
- Rank candidates from best to worst match
- Generate recruiter-style ranking reports

## ✅ Modular Project Architecture
- Service-based design
- Reusable components
- Scalable backend structure

---

# ⚙️ Tech Stack

- Python
- PyMuPDF (PDF parsing)
- Regex / NLP preprocessing
- Modular backend architecture
- Git + GitHub

---

# 📂 Project Structure

```text
adaptive-ai-hiring-platform/
│
├── app/
│   ├── database/              # Future database integration
│   ├── frontend/              # Future Streamlit frontend
│   ├── monitoring/            # Future drift monitoring modules
│   └── services/
│       ├── resume_parser.py
│       ├── information_extractor.py
│       ├── job_description_parser.py
│       ├── matcher.py
│       └── ranking_engine.py
│
├── data/
│   ├── resumes/
│   ├── job_descriptions/
│   └── processed/
│
├── models/                    # Future ML models
├── tests/                     # Future unit tests
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ▶️ How To Run

## 1. Clone Repository

```bash
git clone https://github.com/SaiKavya210804/Adaptive_AI_Hiring_Intelligence_Platform.git
```

---

## 2. Move Into Project Folder

```bash
cd Adaptive_AI_Hiring_Intelligence_Platform
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run The Project

```bash
python main.py
```

---

# 📌 Current Workflow

```text
Resume PDFs
      ↓
Resume Parsing
      ↓
Candidate Information Extraction
      ↓
Job Description Parsing
      ↓
Skill Matching
      ↓
Candidate Ranking
```

---

# 📊 Example Output

```text
===== CANDIDATE RANKINGS =====

Rank #1
Candidate: Sai Kavya Kalyani
Match Percentage: 100.0%

Rank #2
Candidate: Rahul Verma
Match Percentage: 28.57%

Rank #3
Candidate: Ankit Sharma
Match Percentage: 0.0%
```

---

# 🛤️ Future Roadmap

## Phase 1 ✅
- Resume parsing
- Candidate extraction
- JD parsing
- Candidate ranking

## Phase 2
- Semantic similarity using Sentence Transformers
- Embedding-based matching

## Phase 3
- Streamlit recruiter dashboard
- Resume upload interface
- Ranking visualizations

## Phase 4
- Drift monitoring
- Bias monitoring indicators
- Model performance tracking

## Phase 5
- Database integration
- Logging system
- Deployment

---

# 🎯 Project Goal

This project is designed as an explainable and recruiter-friendly AI hiring intelligence prototype.

The focus is on:
- transparency
- modular system design
- ranking explainability
- scalable AI pipeline architecture

rather than black-box automated hiring decisions.

---

# 👩‍💻 Author

Sai Kavya Kalyani

GitHub:
https://github.com/SaiKavya210804