import streamlit as st

from pdf_processor import extract_text_from_pdf
from ai_service import generate_summary, generate_improvements

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

     summary = generate_summary(text)

    improvements = generate_improvements(text)

    st.subheader("AI Summary")
    st.write(summary)

    st.subheader("Resume Improvements")
    st.write(improvements)

    st.subheader("Document Statistics")
    st.write(f"Pages: {page_count}")
    st.write(f"Words: {word_count}")

    st.subheader("Extracted Text")

    st.text_area(
        "Document Content",
        text,
        height=300
    )
