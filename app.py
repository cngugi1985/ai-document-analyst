from bls_service import get_compensation_intelligence
import streamlit as st

import ai_service



from pdf_processor import extract_text_from_pdf
st.set_page_config(
    page_title="CC AI",
    layout="wide"
)

st.title("🚀 CC AI")
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
        current_role = ai_service.extract_current_role(text)

        

    certifications = [
        cert.strip()
        for cert in recommended_certifications.splitlines()
        if cert.strip()
    ]
    recommended_certifications = "\n".join(certifications[:2])

    dashboard_tab, cert_tab, market_tab = st.tabs(
        [
            "📊 Dashboard",
            "🎓 Certifications",
            "📈 Market Intelligence"
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

        st.metric(
            "Pages",
            page_count
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

    with market_tab:

        st.subheader("📈 Market Intelligence")

        selected_state = st.selectbox(
            "Select State",
            [
                "Massachusetts",
                "New Hampshire",
                "Texas",
                "California",
                "Florida"
            ]
        )

        market_data = get_compensation_intelligence(
            current_role,
            selected_state
        )

        st.info(
            "Market Intelligence is currently in preview."
        )

        if market_data:

            st.write(
                f"**Detected Role:** {current_role}"
            )

            st.metric(
                "National Median",
                f"${market_data['national_median']:,}"
            )

            st.metric(
                selected_state,
                f"${market_data['state_compensation']:,}"
            )

            difference = (
                market_data["state_compensation"]
                - market_data["national_median"]
            )

            st.metric(
                "Difference",
                f"${difference:+,}"
            )

            if difference > 0:
                st.success(
                    f"{selected_state} is ${difference:,} above the national median for your role."
                )
            else:
                st.warning(
                    f"{selected_state} is ${abs(difference):,} below the national median for your role."
                )

            st.caption(
                "Source: Bureau of Labor Statistics (Sample Data)"
            )