---

# 📄 JobFit: AI Resume Analyzer

An intelligent resume analyzer built with **Python**, **Streamlit**, and **Google's Gemini AI**. It evaluates your resume against a job description to provide a detailed review and an ATS-style match percentage report.


## 🚀 Features

✅ **AI-Powered Analysis** using Google Gemini
✅ **Dual Analysis Modes**: In-depth review and ATS match percentage
✅ **PDF Resume Parsing** (analyzes the first page)
✅ **Interactive UI** built with Streamlit for a seamless user experience
✅ **Instant Resume Preview** upon upload

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **AI Model**: Google Gemini (`gemini-1.5-flash-latest`)
* **Libraries**: `google-generativeai`, `streamlit`, `PyMuPDF`, `Pillow`

---

## 🧠 How It Works

### Streamlit App (`app.py`)

* The user uploads their PDF resume and pastes a job description into the text area.
* The backend (`input_pdf_setup`) converts the **first page** of the PDF into a JPEG image.
* This image, along with the job description and a specialized prompt, is sent to the Gemini API.
* Two distinct prompts guide the AI: one for a detailed HR review and another for an ATS match report.
* The AI-generated analysis is then displayed clearly in the user interface.

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/your-username/jobfit-resume-analyzer.git](https://github.com/your-username/jobfit-resume-analyzer.git)
cd jobfit-resume-analyzer
### 2️⃣ Create a Virtual Environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3️⃣ Install Dependencies

Create a `requirements.txt` file with the following content:

```plaintext
streamlit
google-generativeai
PyMuPDF
Pillow
```

Then run the installation command:

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your Google Gemini API Key

Create a folder named `.streamlit` in your project directory. Inside it, create a file named `secrets.toml`.

```
.
├── .streamlit/
│   └── secrets.toml
├── app.py
└── requirements.txt
```

Add your API key to `secrets.toml`:

```toml
# .streamlit/secrets.toml
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

Finally, update `app.py` to use this secret:

```python
# In app.py, change this line:
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
```

> 🔑 Get your API key here: [Google AI Studio](https://aistudio.google.com/app/apikey)

---

### 📌 Usage

To run the Streamlit app:

```bash
streamlit run app.py
```

> A web interface will open in your browser. Paste a job description, upload your PDF resume, and choose an analysis type.

---

### 📁 File Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── secrets.toml    # API keys and secrets
└── README.md           # Project documentation
```

---

### ✨ Future Ideas

* Process all pages of the resume, not just the first.
* Add support for more file types like `.docx` and `.txt`.
* Provide actionable suggestions to improve the resume based on the analysis.
* Incorporate a database to save and track analysis history.
* Deploy on Streamlit Community Cloud or Hugging Face Spaces.

---

### 🧑‍💻 Author

* **Your Name** Anand Yadav
* GitHub: [@anandy07](https://github.com/anandy07)

---

### 📜 License

This project is licensed under the MIT License.

---

### ⭐ Contribute & Support

If you liked this project, consider giving it a **star ⭐** on GitHub!
Pull requests, issues, and feature suggestions are always welcome.
