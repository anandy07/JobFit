import base64
import streamlit as st
import os
import io
from PIL import Image
import fitz  # PyMuPDF
import google.generativeai as genai

# ✅ Configure Gemini API with Streamlit Secrets
genai.configure(api_key=st.secrets["AIzaSyBeF5jE-s14lxeMyLvURoU-w9jKp0KhUtg"])

# Convert uploaded PDF to image and then to base64
def input_pdf_setup(uploaded_file):
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded")
    
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    first_page = pdf_document.load_page(0)
    pix = first_page.get_pixmap()
    img_byte_arr = pix.tobytes("jpeg")
    
    pdf_parts = [{
        "mime_type": "image/jpeg",
        "data": base64.b64encode(img_byte_arr).decode()
    }]
    
    image = Image.open(io.BytesIO(img_byte_arr))
    return pdf_parts, image

# Call Gemini API
def get_gemini_response(input_text, pdf_content, job_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-latest') 
    response = model.generate_content([input_text, pdf_content[0], job_prompt])
    return response.text

# ---------- Streamlit UI ----------
st.set_page_config(
    page_title="JobFit",
    page_icon="📄",
    layout="wide"
)

st.title("📄 JobFit")
st.markdown("Analyze your resume against job descriptions with AI-powered insights.")

col1, col2 = st.columns([2, 1])

with col1:
    job_description = st.text_area("Job Description", height=200)
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

with col2:
    if uploaded_file:
        st.success("Resume uploaded successfully!")
        pdf_content, preview_image = input_pdf_setup(uploaded_file)
        st.image(preview_image, caption="Resume Preview", use_container_width=True)

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

if submit_review:
    if uploaded_file:
        response = get_gemini_response(input_prompt_review, pdf_content, job_description)
        st.subheader("Resume Review")
        st.write(response)
    else:
        st.error("Please upload a resume first.")

elif submit_match:
    if uploaded_file:
        response = get_gemini_response(input_prompt_match, pdf_content, job_description)
        st.subheader("ATS Match Results")
        st.write(response)
    else:
        st.error("Please upload a resume first.")
