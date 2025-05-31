import streamlit as st
from transformers import pipeline
import PyPDF2
import random
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["XLA_FLAGS"] = "--xla_hlo_profile=false"

summarizer = pipeline("summarization", model="t5-base")

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def summarize_text(text):
    max_length = min(200, int(0.5 * len(text)))
    chunks = [text[i:i + 1000] for i in range(0, len(text), 1000)]
    summaries = [summarizer(chunk, max_length=max_length, min_length=100, do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)

def generate_questions(summary):
    sentences = summary.split(".")
    questions = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 5:
            answer = random.choice(words)
            question = sentence.replace(answer, "____")
            options = random.sample(words, 3) + [answer]
            random.shuffle(options)
            questions.append((question, answer, options))
    return questions

st.title("📚 AI-Based Class Notes Summarizer")

uploaded_file = st.file_uploader("Upload Lecture Notes (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    st.info("✅ File Uploaded Successfully")
    with st.expander("📄 View Original Content"):
        st.text_area("Lecture Notes", text, height=300)
    if st.button("Summarize Notes"):
        with st.spinner("AI is summarizing your notes..."):
            summary = summarize_text(text)
            st.success("✅ Summarization Complete!")
            st.text_area("🔍 Key Points", summary, height=200)

            st.session_state.summary = summary

# Quiz Mode
if "summary" in st.session_state and st.checkbox("Generate Quiz from Notes"):
    st.subheader("📝 Quiz Mode")
    questions = generate_questions(st.session_state.summary)

    for i, (question, answer, options) in enumerate(questions[:5], 1):
        st.write(f"**Q{i}: {question}**")
        user_answer = st.radio("Choose an option:", options, key=f"q{i}")

        if st.button(f"Check Answer {i}", key=f"check{i}"):
            if user_answer == answer:
                st.success("🎉 Correct!")
            else:
                st.error(f"❌ Wrong! The correct answer is: {answer}")

        def extract_text_from_pdf(uploaded_file):
            extract_text_from_pdf(uploaded_file)
            print("For test purposes only extension of that code uses for makes the Code lengthy and required more Space to store and run. It takes 11.23 MB extra space by extend")
