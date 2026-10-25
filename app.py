import streamlit as st

import ai_service
import salary_service

from pdf_processor import extract_text_from_pdf
st.set_page_config(
    page_title="AI Career Navigator",
    layout="wide"
)

st.title("🚀 AI Career Navigator")

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
    "Upload Resume (PDF)",
    type=["pdf"]
)

location = st.text_input(
    "📍 Target Location",
    value="Manchester, NH"
)

if uploaded_file:

    text, page_count = extract_text_from_pdf(uploaded_file)

    with st.spinner("Analyzing resume..."):

        resume_score = ai_service.generate_resume_score(text)

        summary = ai_service.generate_summary(text)

        improvements = ai_service.generate_improvements(text)

        career_paths = ai_service.generate_career_paths(text)

        skills_to_develop = (
            ai_service.generate_skills_to_develop(text)
        )

        recommended_certifications = (
            ai_service.generate_recommended_certifications(text)
        )

    dashboard_tab, career_tab, cert_tab = st.tabs(
        [
            "📊 Dashboard",
            "🎯 Career Insights",
            "🎓 Certifications"
        ]
    )

    # =========================
    # DASHBOARD
    # =========================

    with dashboard_tab:

        st.metric(
            "Resume Score",
            resume_score
        )

        st.subheader("📄 Summary")

        st.markdown(summary)

        st.divider()

        st.subheader("✅ Resume Improvements")

        st.markdown(improvements)

    # =========================
    # CAREER INSIGHTS
    # =========================

    with career_tab:

        st.subheader("🧭 Career Roadmap")

        roles = [role.strip() for role in career_paths.split("↓")]

        path_labels = [
            "📍 Current Role",
            "🚀 Next Role",
            "🏆 Long-Term Goal"
        ]

        for i, role in enumerate(roles):
            salary_data = salary_service.get_salary_range(
                role,
                location
            )

            card_text = f"""
            {path_labels[i]}

            {role}

            Annual Compensation

            USD {salary_data['min']} to {salary_data['max']}

            Salary Sources

            • {salary_data['source']}

            • {salary_data['source_2']}
            """

            if i == 0:
                st.info(card_text)

            elif i == 1:
                st.success(card_text)

            else:
                st.warning(card_text)

            if i < len(roles) - 1:
                next_role = roles[i + 1]

                next_salary = salary_service.get_salary_range(
                    next_role,
                    location
                )

                increase = salary_service.calculate_increase(
                    salary_data,
                    next_salary
                )

                st.markdown(
                    f"""
**Potential Increase**

USD {increase['min']} to {increase['max']}
"""
                )

            if i < len(roles) - 1:
                st.markdown(
                    "<h1 style='text-align:center;'>⬇️</h1>",
                    unsafe_allow_html=True
                )

        st.divider()

        st.subheader("📈 Skills To Develop")

        st.markdown(skills_to_develop)

    # =========================
    # CERTIFICATIONS
    # =========================

    with cert_tab:

        st.subheader("🎓 Recommended Certifications")

        st.markdown(recommended_certifications)