import pdfplumber
import spacy
import textstat
from collections import Counter
import re

nlp = spacy.load("en_core_web_sm")

KEYWORDS = ['Python', 'SQL', 'Machine Learning', 'Teamwork', 'Communication', 'Leadership', 'Data Analysis']

def analyze_resume(path):
    with pdfplumber.open(path) as pdf:
        text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())

    doc = nlp(text)
    words = [token.text for token in doc if token.is_alpha]
    word_count = len(words)
    keyword_hits = {kw: text.lower().count(kw.lower()) for kw in KEYWORDS}
    most_common = Counter(words).most_common(5)
    readability = textstat.flesch_reading_ease(text)

    feedback = {
        'word_count': word_count,
        'keyword_hits': keyword_hits,
        'most_common_words': most_common,
        'readability': readability
    }

    return feedback
