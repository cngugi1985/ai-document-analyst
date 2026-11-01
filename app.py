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


if uploaded_file:
    text, page_count = extract_text_from_pdf(uploaded_file)

    with st.spinner("Analyzing resume..."):
        resume_score = ai_service.generate_resume_score(text)
        summary = ai_service.generate_summary(text)
        improvements = ai_service.generate_improvements(text)
        skills_to_develop = (
            ai_service.generate_skills_to_develop(text)
        )
        recommended_certifications = (
            ai_service.generate_recommended_certifications(text)
        )

    
    certifications = [
    cert.strip()
    for cert in recommended_certifications.splitlines()
    if cert.strip()
]
    recommended_certifications = "\n".join(certifications[:2])

    dashboard_tab, cert_tab = st.tabs(
        [
            "📊 Dashboard",
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

        st.caption(
            "Extracted directly from the resume before generating career recommendations."
        )

        st.subheader("📄 Summary")

        st.markdown(summary)

        st.divider()

        st.subheader("✅ Resume Improvements")

        st.markdown(improvements)

    # =========================
    # CERTIFICATIONS
    # =========================

    with cert_tab:

        st.subheader("🎓 Recommended Certifications")

        certifications = [
            cert.strip()
            for cert in recommended_certifications.splitlines()
            if cert.strip()
        ]

        for cert in certifications[:2]:
            st.markdown(f"• {cert}")