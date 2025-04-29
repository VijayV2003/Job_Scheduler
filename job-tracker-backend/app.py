import re
import spacy
import pdfplumber
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined job roles and required skills
JOB_ROLES = {
    "Data Scientist": {"skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "SQL", "Data Visualization"]},
    "Data Analyst": {"skills": ["Excel", "SQL", "Power BI", "Python", "Statistics", "Data Cleaning", "Data Visualization"]},
    "Machine Learning Engineer": {"skills": ["Python", "TensorFlow", "PyTorch", "NLP", "Computer Vision", "MLOps", "Model Deployment"]},
    "AI Specialist": {"skills": ["Artificial Intelligence", "Machine Learning", "Neural Networks", "Generative AI", "Big Data", "Cloud Computing"]}
}

@app.get("/")
def home():
    return {"message": "Welcome to the Job Scheduler API"}

@app.post("/process_resume")
async def process_resume(resume: UploadFile = File(...), job_role: str = Form(...)):
    # Extract text from PDF
    extracted_text = extract_text_from_pdf(resume)
    if not extracted_text:
        return {"error": "Failed to extract text from resume"}

    # Extract skills from resume
    extracted_skills = extract_skills(extracted_text)

    # Validate job role
    if job_role not in JOB_ROLES:
        return {"error": f"Invalid job role selected: {job_role}"}

    required_skills = JOB_ROLES[job_role]["skills"]

    # Normalize for comparison
    extracted_skills_lower = set(skill.lower() for skill in extracted_skills)
    required_skills_lower = set(skill.lower() for skill in required_skills)

    # Determine matching and missing skills
    matching_skills = list(required_skills_lower & extracted_skills_lower)
    missing_skills = list(required_skills_lower - extracted_skills_lower)

    # Compute similarity score
    similarity_score = compute_similarity(extracted_text, " ".join(required_skills))

    return {
        "job_role": job_role,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "similarity_score": similarity_score
    }

def extract_text_from_pdf(resume_file):
    """Extracts text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(resume_file.file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text.strip()

def extract_skills(text):
    """Extracts relevant skills from resume text using NLP."""
    doc = nlp(text)
    extracted_skills = set()
    for token in doc:
        if token.ent_type_ in ["ORG", "PRODUCT", "GPE", "WORK_OF_ART"] or token.pos_ in ["NOUN", "PROPN"]:
            extracted_skills.add(token.text)
    return list(extracted_skills)

def compute_similarity(text1, text2):
    """Computes cosine similarity between two texts using TF-IDF."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(similarity[0][0]) * 100, 2)  # return as percentage
