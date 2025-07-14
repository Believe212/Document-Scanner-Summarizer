from transformers import pipeline

# Load model once at the top
# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Hugging Face models have a 1024-token input limit, so truncate
    if len(text) > 3000:
        text = text[:3000]

    try:
        summary_list = summarizer(text, max_length=150, min_length=40, do_sample=False)
        return summary_list[0]['summary_text']
    except Exception as e:
        return f"Summarization failed: {str(e)}"
