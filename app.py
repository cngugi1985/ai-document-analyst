import streamlit as st

from pdf_processor import extract_text_from_pdf
import ai_service
import market_data

st.title("AI Document Analyst")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

overview_tab, career_tab, growth_tab, market_tab = st.tabs(
    [
        "Overview",
        "Career Intelligence",
        "Growth Plan",
        "Market Intelligence"
    ]
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

        career_paths = ai_service.generate_career_paths(text)

        career_roadmap = ai_service.generate_career_roadmap(text)

        skill_gap_analysis = ai_service.generate_skill_gap_analysis(text)

        action_plan = ai_service.generate_action_plan(text)

        recommended_sectors = ai_service.generate_recommended_sectors(text)

        sector_data = market_data.get_market_data("Industrial Automation")

    # ------------------------
    # OVERVIEW TAB
    # ------------------------

    with overview_tab:

        st.metric(
            label="Resume Score",
            value=resume_score
        )

        st.subheader("AI Summary")
        st.write(summary)

        st.subheader("Resume Improvements")
        st.write(improvements)

    # ------------------------
    # CAREER INTELLIGENCE TAB
    # ------------------------

    with career_tab:

        st.subheader("Career Blind Spots")
        st.write(career_blindspots)

        st.subheader("Recommended Career Paths")
        st.write(career_paths)

    # ------------------------
    # GROWTH PLAN TAB
    # ------------------------

    with growth_tab:

        st.subheader("30-Day Action Plan")
        st.write(action_plan)

        st.subheader("Career Roadmap")
        st.write(career_roadmap)

        st.subheader("Skill Gap Analysis")
        st.write(skill_gap_analysis)

    # ------------------------
    # MARKET INTELLIGENCE TAB
    # ------------------------

    with market_tab:

        st.subheader("Recommended Sectors")

        st.write(recommended_sectors)


        st.subheader("Market Snapshot")

        st.write(
            f"Salary Range: {sector_data['salary_range']}"
        )

        st.write(
            f"Demand: {sector_data['demand']}"
        )

        st.write(
            f"Growth Outlook: {sector_data['growth']}"
        )

        st.subheader("Recommended Certifications")

        for certification in sector_data["certifications"]:
            st.write(f"• {certification}")

    # ------------------------
    # DOCUMENT DETAILS
    # ------------------------

    st.subheader("Document Statistics")

    st.write(f"Pages: {page_count}")
    st.write(f"Words: {word_count}")

    st.subheader("Extracted Text")

    st.text_area(
        "Document Content",
        text,
        height=300
    )