import streamlit as st

import ai_service
from pdf_processor import extract_text_from_pdf

st.set_page_config(
    page_title="AI Career Intelligence",
    layout="wide"
)

st.title("🚀 AI Career Intelligence")

st.markdown("""
<style>

div[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    text, page_count = extract_text_from_pdf(uploaded_file)

    word_count = len(text.split())

    with st.spinner("Analyzing your resume..."):

        summary = ai_service.generate_summary(text)

        improvements = ai_service.generate_improvements(text)

        resume_score = ai_service.generate_resume_score(text)

        career_paths = ai_service.generate_career_paths(text)

        blind_spots = ai_service.generate_career_blindspots(text)

        Skills_To_Develop = ai_service.generate_Skills_To_Develop(text)

        action_plan = ai_service.generate_action_plan(text)


        market_intelligence = ai_service.generate_market_intelligence(text)

        recommended_certifications = (
            ai_service.generate_recommended_certifications(text)
        )

    dashboard_tab, insights_tab, market_tab = st.tabs(
        [
            "📊 Dashboard",
            "🎯 Career Insights",
            "🎓 Certifications"
        ]
    )

    # ==================================================
    # DASHBOARD
    # ==================================================

    with dashboard_tab:

       

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Resume Score",
                resume_score
            )

        

    # ==================================================
    # CAREER INSIGHTS
    # ==================================================

    with insights_tab:

        st.subheader("🧭 Recommended Career Paths")
        st.markdown(career_paths)

        st.divider()

        

        st.subheader("📈 Skill To Develop")
        st.markdown(Skills_To_Develop)

        st.divider()

     

    # ==================================================
    # MARKET INTELLIGENCE
    # ==================================================

    with market_tab:

        

        st.subheader("⚠ Reccomended Certifications")

        st.markdown(recommended_certifications)

        st.divider()

        
        
