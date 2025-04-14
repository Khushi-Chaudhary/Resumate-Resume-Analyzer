import re
from collections import Counter
from textstat import flesch_reading_ease

# Action verbs and soft skills sets
ACTION_VERBS = {
    'led', 'developed', 'created', 'designed', 'implemented', 'analyzed',
    'managed', 'built', 'initiated', 'executed', 'organized'
}

SOFT_SKILLS = {
    'teamwork', 'communication', 'leadership', 'collaboration',
    'problem-solving', 'time management'
}

def analyze_resume(text):
    """
    Analyze the resume and return basic metrics like word count, readability score, and frequent words.
    """
    # Basic text analysis
    word_count = len(text.split())
    readability_score = flesch_reading_ease(text)
    
    # Frequent words analysis
    word_counter = Counter(re.findall(r'\b\w+\b', text.lower()))
    most_common_words = word_counter.most_common(5)
    
    # Keyword presence
    keywords = ['python', 'sql', 'machine learning', 'teamwork', 'communication', 'leadership', 'data analysis']
    keyword_counts = {keyword: word_counter[keyword] for keyword in keywords}

    return {
        "word_count": word_count,
        "readability_score": readability_score,
        "top_words": most_common_words,
        "keyword_counts": keyword_counts
    }

def get_extra_metrics(text):
    """
    Return extra metrics such as bullet-to-paragraph ratio, action verbs count, and soft skills found.
    """
    lines = text.split('\n')
    
    # Count bullet points
    bullet_points = [line for line in lines if line.strip().startswith(("-", "•", "*"))]
    num_bullets = len(bullet_points)
    
    # Count paragraph-style lines (not empty and not bullets)
    paragraphs = [line for line in lines if line.strip() and not line.strip().startswith(("-", "•", "*"))]
    num_paragraphs = len(paragraphs)
    
    bullet_ratio = (num_bullets / (num_bullets + num_paragraphs)) * 100 if (num_bullets + num_paragraphs) > 0 else 0

    # Action verbs at sentence start
    sentences = re.split(r'[.\n]', text)
    action_verb_count = sum(1 for s in sentences if s.strip().split(" ")[0].lower() in ACTION_VERBS)

    # Soft skills detection
    word_counter = Counter(re.findall(r'\b\w+\b', text.lower()))
    soft_skills_found = {skill: word_counter[skill] for skill in SOFT_SKILLS if word_counter[skill] > 0}

    return {
        "bullet_points": num_bullets,
        "paragraphs": num_paragraphs,
        "bullet_ratio": round(bullet_ratio, 2),
        "action_verbs_count": action_verb_count,
        "soft_skills_found": soft_skills_found,
        "soft_skills_score": len(soft_skills_found)
    }
