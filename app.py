import streamlit as st

import ai_service

import market_data
from pdf_processor import extract_text_from_pdf

st.set_page_config(
    page_title="AI Document Analyst",
    layout="wide"
)

st.title("AI Document Analyst")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    text, page_count = extract_text_from_pdf(uploaded_file)
    word_count = len(text.split())

    with st.spinner("Analyzing resume..."):
        summary = ai_service.generate_summary(text)
        improvements = ai_service.generate_improvements(text)
        resume_score = ai_service.generate_resume_score(text)
        career_paths = ai_service.generate_career_paths(text)
        blind_spots = ai_service.generate_career_blindspots(text)
        skill_gap_analysis = ai_service.generate_skill_gap_analysis(text)
        action_plan = ai_service.generate_action_plan(text)
        career_roadmap = ai_service.generate_career_roadmap(text)
        primary_sector = ai_service.generate_primary_sector(text)
        primary_role = ai_service.generate_primary_role(text)
        market_intelligence = ai_service.generate_market_intelligence(text)
        existing_certifications = ai_service.generate_existing_certifications(text)


    overview_tab, career_tab, growth_tab, market_tab = st.tabs(
        [
            "Overview",
            "Career Intelligence",
            "Growth Plan",
            "Market Intelligence",
        ]
    )

    with overview_tab:
        st.subheader("Resume Score")
        st.write(resume_score)

        st.subheader("AI Summary")
        st.write(summary)

        st.subheader("Resume Improvements")
        st.write(improvements)

        st.subheader("Document Statistics")
        st.write(f"Pages: {page_count}")
        st.write(f"Words: {word_count}")

        st.subheader("Extracted Text")
        st.text_area(
            "Content",
            text,
            height=300,
        )

    with career_tab:
        st.subheader("Recommended Career Paths")

        st.write(career_paths)

        st.subheader("Career Blind Spots")

        st.write(blind_spots)

    with growth_tab:
        st.subheader("Skill Gap Analysis")

        st.write(skill_gap_analysis)

        st.subheader("30-Day Action Plan")

        st.write(action_plan)

        st.subheader("Career Roadmap")

        st.write(career_roadmap)

    with market_tab:
        st.subheader("Primary Role")

        st.write(primary_role)

        st.subheader("AI Market Intelligence")

        st.text(market_intelligence)
        st.subheader("Primary Sector")

        st.write(primary_sector)
        st.subheader("Existing Certifications")

        st.write(existing_certifications)
