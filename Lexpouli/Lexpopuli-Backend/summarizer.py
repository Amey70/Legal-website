from transformers import pipeline
from deep_translator import GoogleTranslator

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):

    if len(text) < 100:
        return text

    summary = summarizer(
        text,
        max_length=200,
        min_length=60,
        do_sample=False
    )

    return summary[0]['summary_text']


def translate_text(text, language):

    if language == "en":
        return text

    if language == "fr":
        lang = "hi"

    elif language == "es":
        lang = "mr"

    else:
        lang = "en"

    translated = GoogleTranslator(source='auto', target=lang).translate(text)

    return translated