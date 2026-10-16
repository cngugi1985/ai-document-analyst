import streamlit as st

from pdf_processor import extract_text_from_pdf
import ai_service

st.title("AI Document Analyst")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF uploaded successfully!")

    text, page_count = extract_text_from_pdf(uploaded_file)
    word_count = len(text.split())

    with st.spinner("Analyzing resume..."):
        summary = ai_service.generate_summary(text)

    improvements = ai_service.generate_improvements(text)

    resume_score = ai_service.generate_resume_score(text)

    career_blindspots = ai_service.generate_career_blindspots(text)

    skill_gap_analysis = ai_service.generate_skill_gap_analysis(text)

    career_paths = ai_service.generate_career_paths(text)

    career_roadmap = ai_service.generate_career_roadmap(text)
    st.metric(
        label="Resume Score",
        value=resume_score
    )

    st.subheader("AI Summary")
    st.write(summary)

    st.subheader("Resume Improvements")
    st.write(improvements)
    st.subheader("Career Blindspots")
    st.write(career_blindspots)
    st.subheader("Recommended Career Paths")

    st.write(career_paths)
    st.subheader("Career Roadmap")

    st.write(career_roadmap)
    st.subheader("Skill Gap Analysis")
    st.write(skill_gap_analysis)

    st.subheader("Document Statistics")
    st.write(f"Pages: {page_count}")
    st.write(f"Words: {word_count}")

    st.subheader("Extracted Text")

    st.text_area(
        "Document Content",
        text,
        height=300
    )
