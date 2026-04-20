import streamlit as st
import spacy
from pdfminer.high_level import extract_text
from keyword_matcher import calculate_similarity

nlp = spacy.load("en_core_web_sm")


st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")


st.title("📄 AI Resume Analyzer")
st.subheader("Check how well your resume matches a job description")

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area("💼 Paste Job Description")

st.markdown("---")

def extract_resume_text(file):
    return extract_text(file)

if uploaded_file and job_description:

    resume_text = extract_resume_text(uploaded_file)

    similarity = calculate_similarity(resume_text, job_description)

    ats_score = round(similarity * 10, 2)

    st.subheader("🎯 ATS Resume Score")

    st.progress(similarity)

    st.metric(label="Resume Match Score", value=f"{ats_score} / 10")


    if ats_score < 5:
        st.error("⚠ Your resume needs improvement. Add more relevant skills and keywords.")
    elif ats_score < 8:
        st.warning("👍 Good match but you can improve by adding more job-specific keywords.")
    else:
        st.success("✅ Excellent match! Your resume fits this job well.")

    st.markdown("---")

    st.subheader("💡 Suggestions to Improve")

    suggestions = []

    if "python" not in resume_text.lower():
        suggestions.append("Add Python skills if relevant.")

    if "machine learning" not in resume_text.lower():
        suggestions.append("Include Machine Learning projects.")

    if "sql" not in resume_text.lower():
        suggestions.append("Mention SQL or database experience.")

    if suggestions:
        for s in suggestions:
            st.write("•", s)
    else:
        st.write("Your resume already includes key skills!")