class _DummyTab:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class st:
    """A small, self-contained streamlit-like API used by this app."""

    @staticmethod
    def title(message):
        print(f"[TITLE] {message}")

    @staticmethod
    def file_uploader(label, type=None):
        return None

    @staticmethod
    def tabs(labels):
        return tuple(_DummyTab(label) for label in labels)

    @staticmethod
    def success(message):
        print(f"[SUCCESS] {message}")

    @staticmethod
    def spinner(message):
        class _Spinner:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                return False

        return _Spinner()

    @staticmethod
    def metric(label, value):
        print(f"[METRIC] {label}: {value}")

    @staticmethod
    def subheader(label):
        print(f"[SUBHEADER] {label}")

    @staticmethod
    def write(*values):
        print(*values)

    @staticmethod
    def text_area(label, value, height=300):
        print(f"[TEXT AREA: {label}]\n{value}")


from pdf_processor import extract_text_from_pdf
import ai_service
import market_data
import certification_utils

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

        primary_sector = ai_service.generate_primary_sector(text)


        existing_certifications = ai_service.generate_existing_certifications(text)

    certification_list = existing_certifications.split("\n")

    normalized_certifications = []

    for cert in certification_list:

        normalized_certifications.append(
            certification_utils.normalize_certification(cert)
        )

    sector_data = market_data.get_market_data(primary_sector)
    missing_certifications = (
    certification_utils.find_missing_certifications(
        certification_list,
        sector_data["certifications"]
    )
)

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

        st.write(f"Primary Sector: {primary_sector}")

        #st.subheader("Existing Certifications Found")

        #st.write(existing_certifications)

        #st.subheader("Normalized Certifications")

        #st.write(normalized_certifications)


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

        st.subheader("Certification Gap Analysis")

        for certification in missing_certifications:
            st.write(f"⚠ {certification}")

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