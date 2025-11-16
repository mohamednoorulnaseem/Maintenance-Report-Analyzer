import streamlit as st
import traceback
import os

try:
    from helper import extract_text, summarize_text, answer_question
except Exception as e:
    st.error("Failed to import helper module")
    st.code(traceback.format_exc())
    st.stop()

st.title("🛠 Maintenance Report Analyzer")

uploaded_pdf = st.file_uploader("Upload a maintenance report (PDF)", type="pdf")

if uploaded_pdf:
    try:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_pdf.read())
        st.success("PDF uploaded successfully!")
    except Exception as e:
        st.error("Failed to save PDF")
        st.code(traceback.format_exc())
        st.stop()

    try:
        with st.spinner("Extracting text..."):
            text = extract_text("temp.pdf")
        if not text or not text.strip():
            st.warning("No text extracted from PDF")
            st.stop()
    except Exception:
        st.error("Error extracting text from PDF")
        st.code(traceback.format_exc())
        st.stop()

    st.subheader("📄 Extracted Summary")
    try:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
        st.write(summary)
    except Exception:
        st.error("Error during summarization")
        st.code(traceback.format_exc())

    st.subheader("❓ Ask Questions from the Report")
    question = st.text_input("Enter your question")

    if question:
        try:
            with st.spinner("Processing question..."):
                answer = answer_question(question, text)
            st.write("**Answer:**", answer)
        except Exception:
            st.error("Error answering question")
            st.code(traceback.format_exc())

    try:
        os.remove("temp.pdf")
    except:
        pass