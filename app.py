import streamlit as st

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

    st.success("PDF processed successfully!")

    st.subheader("Document Statistics")

    st.write(f"Pages: {page_count}")
    st.write(f"Words: {word_count}")

    st.subheader("Extracted Text")

    st.text_area(
        "Content",
        text,
        height=300
    )