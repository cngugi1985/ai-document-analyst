import streamlit as st
from pypdf import PdfReader

st.title("AI Document Analyst")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF uploaded successfully!")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text

    word_count = len(text.split())

    st.subheader("Document Statistics")

    st.write(f"Pages: {len(reader.pages)}")
    st.write(f"Words: {word_count}")

    st.subheader("Extracted Text")

    st.text_area(
        "Document Content",
        text,
        height=300)