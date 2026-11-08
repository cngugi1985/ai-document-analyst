from bls_service import get_compensation_intelligence
from states import US_STATES
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

    market_tab, dashboard_tab, cert_tab = st.tabs(
    [
        "📈 Market Intelligence",
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

    

        # st.subheader("📄 Summary")

        # st.markdown(summary)

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

            # =========================
    # MARKET INTELLIGENCE
    # =========================

    with market_tab:

        st.subheader("📈 Market Intelligence")

        col1, col2, col3 = st.columns(3)

        with col1:
            state_1 = st.selectbox(
                "State 1",
                US_STATES,
                index=4
            )

        with col2:
            state_2 = st.selectbox(
                "State 2",
                US_STATES,
                index=43
            )

        with col3:
            state_3 = st.selectbox(
                "State 3",
                US_STATES,
                index=29
            )

        market_data_1 = get_compensation_intelligence(
            current_role,
            state_1
        )

        
        market_data_2 = get_compensation_intelligence(
            current_role,
            state_2
        )

        market_data_3 = get_compensation_intelligence(
            current_role,
            state_3
        )

        available_market_data = [
            (state_1, market_data_1),
            (state_2, market_data_2),
            (state_3, market_data_3)
        ]

        available_market_data = [
            item
            for item in available_market_data
            if item[1]
        ]

        if len(available_market_data) >= 2:

            highest = max(
                available_market_data,
                key=lambda x: x[1]["state_compensation"]
            )

            lowest = min(
                available_market_data,
                key=lambda x: x[1]["state_compensation"]
            )

            gap = (
                highest[1]["state_compensation"]
                - lowest[1]["state_compensation"]
            )

            

            ranked_states = sorted(
                available_market_data,
                key=lambda x: x[1]["state_compensation"],
                reverse=True
            )

            medals = {}

            for i, (state, data) in enumerate(
                ranked_states,
                start=1
            ):
                medals[state] = {
                    1: "🥇",
                    2: "🥈",
                    3: "🥉"
                }.get(i, "")

            comparison_col1, comparison_col2, comparison_col3 = st.columns(3)

            with comparison_col1:

                st.markdown(
    f"### {medals.get(state_1,'')} {state_1}"
)

                if market_data_1:
                    st.metric(
                        "Annual Wage",
                        f"${market_data_1['state_compensation']:,}"
                    )

            with comparison_col2:

                st.markdown(
    f"### {medals.get(state_2,'')} {state_2}"
)

                if market_data_2:
                    st.metric(
                        "Annual Wage",
                        f"${market_data_2['state_compensation']:,}"
                    )

            with comparison_col3:

                st.markdown(
    f"### {medals.get(state_3,'')} {state_3}"
)

                if market_data_3:
                    st.metric(
                        "Annual Wage",
                        f"${market_data_3['state_compensation']:,}"
                    )

            st.divider()

        st.write(current_role)

       
        st.caption(
            "Source: Bureau of Labor Statistics (OEWS Wage Data)"
        )