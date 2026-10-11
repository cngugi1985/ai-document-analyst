import streamlit as st

from pdf_processor import extract_text_from_pdf

st.title("AI Document Analyst")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF uploaded successfully!")

    text, page_count = extract_text_from_pdf(uploaded_file)

    word_count = len(text.split())

    st.subheader("Document Statistics")

    st.write(f"Pages: {page_count}")
    st.write(f"Words: {word_count}")

    st.subheader("Extracted Text")

    st.text_area(
        "Document Content",
        text,
        height=300
    )