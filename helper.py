import pdfplumber
from transformers import pipeline

# Load summarization and QA models (these download on first run)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def extract_text(pdf_path):
    """Extract text from PDF file."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting text: {e}")
    return text

def summarize_text(text, max_length=150, min_length=50):
    """Summarize extracted text using BART model."""
    if not text or len(text.split()) < 50:
        return "Text too short to summarize."
    
    try:
        # Split into chunks if text is very long
        chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
        summaries = []
        
        for chunk in chunks:
            if len(chunk.split()) >= 20:
                summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
                summaries.append(summary[0]["summary_text"])
        
        return " ".join(summaries) if summaries else "Could not summarize text."
    except Exception as e:
        return f"Summarization error: {str(e)}"

def answer_question(question, context):
    """Answer questions based on extracted text context."""
    if not context or not question:
        return "Context or question is empty."
    
    try:
        result = qa_pipeline(question=question, context=context)
        return result["answer"]
    except Exception as e:
        return f"QA error: {str(e)}"
