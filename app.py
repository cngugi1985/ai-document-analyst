import streamlit as st

st.set_page_config(
    page_title="AI Document Analyst",
    layout="wide"
)

st.title("AI Document Analyst")

st.success("✅ Streamlit is working")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF uploaded successfully!")