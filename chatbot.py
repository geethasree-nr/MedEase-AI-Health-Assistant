# ============================================
#   MedEase — NLP Engine
#   Concepts: Tokenization, Stop Word Removal,
#             Lemmatization, TF-IDF, Cosine Similarity
# ============================================

import nltk
import string
import numpy as np
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data.knowledge_base import questions, answers

# Download required NLTK data
nltk.download('punkt',     quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet',   quiet=True)
nltk.download('punkt_tab', quiet=True)

# ── Initialize NLP tools ──────────────────────────────────────
lemmatizer = WordNetLemmatizer()
stop_words  = set(stopwords.words('english'))

# ── Preprocessing Pipeline ────────────────────────────────────
def preprocess(text):
    """
    NLP Pipeline:
    1. Lowercase
    2. Remove special characters
    3. Tokenize
    4. Remove punctuation & stop words
    5. Lemmatize
    """
    text   = text.lower()
    text   = re.sub(r'[^a-zA-Z\u0B80-\u0BFF\s]', ' ', text)  # keep Tamil unicode too
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

# ── Vectorize Knowledge Base ──────────────────────────────────
processed_questions = [preprocess(q) for q in questions]

vectorizer   = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)

# ── BMI Calculator ────────────────────────────────────────────
def calculate_bmi(text):
    """
    Detect weight & height from user message and compute BMI.
    Example: 'my weight is 65 kg and height is 170 cm'
    """
    weight = re.search(r'(\d+)\s*kg', text, re.IGNORECASE)
    height = re.search(r'(\d+)\s*cm', text, re.IGNORECASE)

    if weight and height:
        w = float(weight.group(1))
        h = float(height.group(1)) / 100  # convert cm to m
        bmi = round(w / (h ** 2), 1)

        if bmi < 18.5:
            category = "Underweight 🔵"
            tip = "Try to eat more nutritious, calorie-rich foods and consult a doctor."
        elif 18.5 <= bmi < 25:
            category = "Normal weight ✅"
            tip = "Great! Maintain your healthy lifestyle."
        elif 25 <= bmi < 30:
            category = "Overweight 🟡"
            tip = "Focus on a balanced diet and regular exercise."
        else:
            category = "Obese 🔴"
            tip = "Please consult a doctor and consider a structured diet & fitness plan."

        return (
            f"📊 Your BMI Result:\n\n"
            f"• Weight : {w} kg\n"
            f"• Height : {height.group(1)} cm\n"
            f"• BMI    : {bmi}\n"
            f"• Status : {category}\n\n"
            f"💡 Tip: {tip}"
        )
    return None

# ── Main Chatbot Response Function ───────────────────────────
def detect_sentiment(text):
    sad_words = ["sad", "depressed", "lonely", "hopeless", "crying",
                 "unhappy", "miserable", "tired", "low", "down", "upset"]
    stress_words = ["stressed", "anxious", "anxiety", "worried", "panic",
                    "overwhelmed", "nervous", "fear", "tension"]
    angry_words = ["angry", "frustrated", "irritated", "mad", "furious"]

    text_lower = text.lower()

    if any(w in text_lower for w in sad_words):
        return "sad"
    elif any(w in text_lower for w in stress_words):
        return "stress"
    elif any(w in text_lower for w in angry_words):
        return "angry"
    return None
def get_response(user_input, threshold=0.15):
    """
    Main function:
    1. Check for BMI calculation request
    2. Preprocess user input
    3. Vectorize & compute cosine similarity
    4. Return best matching answer or fallback
    """
    sentiment = detect_sentiment(user_input)
    if sentiment == "sad":
        return ("💛 I can sense you're feeling low today. That's okay — you're not alone!\n\n"
                "• Talk to someone you trust\n"
                "• Go for a short walk in fresh air\n"
                "• Listen to your favourite music\n"
                "• Eat something you love 🍽️\n\n"
                "If this feeling continues for more than 2 weeks, please consult a doctor. You matter! 💛")
    elif sentiment == "stress":
        return ("🧘 I can sense you're stressed. Take a deep breath — it's going to be okay!\n\n"
                "• Inhale 4 sec → Hold 4 sec → Exhale 4 sec\n"
                "• Try 10 minutes of meditation\n"
                "• Drink a glass of water\n"
                "• Step away from screen for 5 minutes\n\n"
                "You've got this! 💪")
    elif sentiment == "angry":
        return ("😤 Feeling frustrated? Completely valid!\n\n"
                "• Take 5 deep slow breaths\n"
                "• Go for a brisk walk\n"
                "• Write down what's bothering you\n"
                "• Drink cold water\n\n"
                "Things will get better! 🌿")

    comparison = compare_foods(user_input)
    """
    Main function:
    1. Check for BMI calculation request
    2. Preprocess user input
    3. Vectorize & compute cosine similarity
    4. Return best matching answer or fallback
    """
    comparison = compare_foods(user_input)
    if comparison:
        return comparison
    # Check for BMI calculation
    if re.search(r'\d+', user_input) and \
   ('kg' in user_input.lower() or 'kilo' in user_input.lower()) and \
   ('cm' in user_input.lower() or 'height' in user_input.lower()):
        bmi_result = calculate_bmi(user_input)
        if bmi_result:
            return bmi_result

    # Preprocess input
    processed_input = preprocess(user_input)

    if not processed_input.strip():
        return "Could you please describe your health concern in more detail? 🤔"

    # Vectorize and compute similarity
    user_vec     = vectorizer.transform([processed_input])
    similarities = cosine_similarity(user_vec, tfidf_matrix).flatten()

    best_idx   = int(np.argmax(similarities))
    best_score = similarities[best_idx]

    if best_score >= threshold:
        return answers[best_idx]
    else:
        return (
            "I'm not sure about that. Try asking me about:\n\n"
            "• Symptoms: fever, headache, cold, stomach pain\n"
            "• Diet: idli, dosa, rice, dal nutrition\n"
            "• BMI: 'My weight is 65 kg and height is 170 cm'\n"
            "• Wellness: sleep, stress, immunity, water intake\n"
            "• Fitness: workout, yoga"
        )
def compare_foods(user_input):
    """
    Detects 'compare X vs Y' or 'compare X and Y' pattern
    and returns both nutrition answers side by side.
    """
    match = re.search(
        r'compare\s+(.+?)\s+(?:vs|and|versus)\s+(.+)',
        user_input, re.IGNORECASE
    )
    if match:
        food1 = match.group(1).strip() + " nutrition"
        food2 = match.group(2).strip() + " nutrition"
        ans1 = get_response(food1)
        ans2 = get_response(food2)
        return f"🔵 {food1.upper()}\n{ans1}\n\n🟢 {food2.upper()}\n{ans2}"
    return None