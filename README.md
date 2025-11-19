# 📄 Maintenance Report Analyzer

A Python-based tool for **extracting text from PDF maintenance reports**,  
performing **summarization**, and enabling **question answering** using LLMs.

---

## 🚀 Features

- 🔍 **PDF Text Extraction**  
  Extracts content from multi-page PDF maintenance reports.

- 🧠 **Intelligent Summarization**  
  Summarizes long technical documents using LLMs.

- ❓ **Question Answering**  
  Ask questions about the extracted report directly.

- ⚙️ **Streamlit Web UI**  
  Simple and intuitive interface for uploading PDFs and interacting with summaries.

---

## 📂 Project Structure

```
Maintenance-Report-Analyzer/
│── app.py               # Streamlit app
│── helper.py            # Helper functions for LLM, PDF extraction
│── requirements.txt     # Dependencies
│── Set-ExecutionPolicy  # Windows helper file
│── .gitignore
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🔧 Technologies Used

- Python
- PyPDF2 / pdfplumber
- Streamlit
- LangChain (if used)
- OpenAI / LLM API

---

## 📌 Future Improvements

- Add support for tables inside PDFs
- Add multi-language summarization
- Add export-to-PDF feature for summaries

---

## 👨‍💻 Author

**Mohamed Noorul Naseem**  
GitHub: https://github.com/mohamednoorulnaseem
