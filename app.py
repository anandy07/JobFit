from dotenv import load_dotenv
import streamlit as st
import os
import fitz  # PyMuPDF
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded")

    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text() + "\n"
    return text.strip()

# Call Gemini API
def get_gemini_response(input_text, resume_text, job_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-latest') 
    response = model.generate_content([
        input_text,
        f"Resume Content:\n{resume_text}",
        f"Job Description:\n{job_prompt}"
    ])
    return response.text

# ---------- Streamlit UI ----------
st.set_page_config(
    page_title="JobFit",
    page_icon="📄",
    layout="wide"
)

# Page Title
st.title("📄 JobFit")
st.markdown("Analyze your resume against job descriptions with AI-powered insights.")

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    job_description = st.text_area("Job Description", height=200)
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

with col2:
    if uploaded_file:
        st.success("Resume uploaded successfully!")
        # Just preview first page as image (optional)
        pdf_preview = fitz.open(stream=uploaded_file.getvalue(), filetype="pdf")
        pix = pdf_preview[0].get_pixmap()
        st.image(pix.tobytes("png"), caption="Resume Preview", use_container_width=True)

# Action Buttons
st.markdown("---")
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    submit_review = st.button("🔍 Review Resume")
with col_btn2:
    submit_match = st.button("📊 Check Match Percentage")

# Prompts
input_prompt_review = """
You are an experienced HR with technical expertise in Machine Learning, Deep Learning, Data Science, and Software Development.
Review the provided resume against the job description. Highlight strengths and weaknesses clearly.
"""

input_prompt_match = """
You are an ATS (Applicant Tracking System) expert.
Evaluate the resume against the provided job description. 
Output format:
1. Percentage match
2. Keywords missing
3. Final thoughts
"""

# Results Section
if submit_review:
    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
        response = get_gemini_response(input_prompt_review, resume_text, job_description)
        st.subheader("Resume Review")
        st.write(response)
    else:
        st.error("Please upload a resume first.")

elif submit_match:
    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)
        response = get_gemini_response(input_prompt_match, resume_text, job_description)
        st.subheader("ATS Match Results")
        st.write(response)
    else:
        st.error("Please upload a resume first.")
