# 🌿 MedEase — AI Health Assistant

A multilingual (Tamil + English) AI-powered health chatbot built using NLP techniques, designed for Indian users — especially targeting rural healthcare accessibility.

---

## 🚀 Features

- 🤒 **Symptom Checker** — Get first-aid advice for common symptoms
- 📊 **BMI Calculator** — Just type your weight and height
- 🥗 **Indian Diet Advisor** — Nutrition info for idli, dosa, rice, dal and more
- 😴 **Sleep & Wellness Tips**
- 🧘 **Stress & Mood Support**
- 🏋️ **Fitness Recommendations**
- 🌐 **Tamil + English Support**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| NLTK | Tokenization, Stop words, Lemmatization |
| Scikit-learn | TF-IDF Vectorization, Cosine Similarity |
| Streamlit | Web UI |
| NumPy | Vector operations |

---

## 📁 Project Structure

```
medease/
│
├── app.py                  ← Streamlit web app (UI)
├── chatbot.py              ← NLP engine
├── data/
│   └── knowledge_base.py  ← Q&A knowledge base
├── requirements.txt        ← Dependencies
└── README.md
```

---

## ⚙️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/medease.git
cd medease

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 🧠 NLP Concepts Used

| Concept | Where Used |
|---|---|
| Tokenization | `word_tokenize()` in chatbot.py |
| Stop Word Removal | `nltk.corpus.stopwords` |
| Lemmatization | `WordNetLemmatizer` |
| TF-IDF Vectorization | `TfidfVectorizer` |
| Cosine Similarity | Matching user query to knowledge base |
| Regex | BMI extraction from natural language |

---

## ⚠️ Disclaimer

MedEase is for **informational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified doctor.

---

## 👨‍💻 Author

Built as a final year project — combining NLP and real-world health impact for rural India 🇮🇳
