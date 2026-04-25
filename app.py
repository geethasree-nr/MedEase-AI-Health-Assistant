# ============================================
#   MedEase — Streamlit Web App
#   Run: streamlit run app.py
# ============================================

import streamlit as st
import time
from chatbot import get_response

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="MedEase — AI Health Assistant",
    page_icon="🌿",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #f7faf9; }
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 1.5px solid #1D9E75;
        padding: 10px 20px;
        font-size: 15px;
    }
    .stButton > button {
        background-color: #1D9E75;
        color: white;
        border-radius: 25px;
        padding: 8px 24px;
        border: none;
        font-size: 15px;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #0F6E56;
    }
    .chat-bubble-user {
        background-color: #1D9E75;
        color: white;
        padding: 12px 18px;
        border-radius: 18px 18px 4px 18px;
        margin: 6px 0;
        max-width: 80%;
        margin-left: auto;
        font-size: 15px;
    }
    .chat-bubble-bot {
        background-color: #ffffff;
        color: #1a1a1a;
        padding: 12px 18px;
        border-radius: 18px 18px 18px 4px;
        margin: 6px 0;
        max-width: 80%;
        border: 1px solid #e0f0ea;
        font-size: 15px;
        line-height: 1.6;
    }
    .chat-name-user { text-align: right; font-size: 12px; color: #888; margin-bottom: 2px; }
    .chat-name-bot  { font-size: 12px; color: #1D9E75; margin-bottom: 2px; font-weight: 600; }
    .disclaimer {
        background-color: #fff8e1;
        border-left: 4px solid #EF9F27;
        padding: 10px 14px;
        border-radius: 6px;
        font-size: 13px;
        color: #6d5200;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────

with st.sidebar:
    st.image("https://img.icons8.com/color/96/caduceus.png", width=70)
    st.title("MedEase 🌿")
    st.caption("AI Health Assistant — Tamil & English")
    st.markdown("---")

    st.markdown("### 🔍 Nutrition Explorer")
    category = st.selectbox("Choose a category:", [
        "🩺 Health Topics",
        "🍎 Fruits",
        "🥜 Nuts & Seeds",
        "🥦 Vegetables",
        "🍚 Indian Foods",
        "🍗 Meat & Seafood",
        "🥤 Juices",
        "🫘 Soya & Legumes",
        "🌱 Sprouts",
        "🌾 Millets",
        "🌾 Grains"
    ])

    st.markdown("---")

    food_map = {
        "🩺 Health Topics": [
            "I have fever and headache",
            "I feel stressed and anxious",
            "Tips for better sleep",
            "Diet plan for weight loss",
            "Beginner workout plan",
            "How to boost immunity",
        ],
        "🍎 Fruits": [
            "Apple nutrition", "Mango nutrition", "Orange nutrition",
            "Banana nutrition", "Guava nutrition", "Pomegranate nutrition",
            "Papaya nutrition", "Watermelon nutrition", "Amla nutrition"
        ],
        "🥜 Nuts & Seeds": [
            "Almond nutrition", "Walnut nutrition", "Cashew nutrition",
            "Peanut nutrition", "Pista nutrition", "Flaxseed nutrition",
            "Chia seed nutrition", "Sunflower seed nutrition"
        ],
        "🥦 Vegetables": [
            "Spinach nutrition", "Carrot nutrition", "Tomato nutrition",
            "Broccoli nutrition", "Bitter gourd nutrition", "Drumstick nutrition",
            "Sweet potato nutrition", "Onion nutrition", "Garlic nutrition"
        ],
        "🍚 Indian Foods": [
            "Idli nutrition", "Dosa nutrition", "Sambar nutrition",
            "Rice nutrition", "Dal nutrition", "Chapati nutrition",
            "Paneer nutrition", "Curd nutrition",
            "Upma nutrition", "Milk nutrition", "Coconut water nutrition"
        ],
        "🍗 Meat & Seafood": [
            "Chicken nutrition", "Beef nutrition", "Mutton nutrition",
            "Fish nutrition", "Prawn nutrition", "Tuna nutrition", "Turkey nutrition"
        ],
        "🥤 Juices": [
            "Orange juice nutrition", "Carrot juice nutrition", "Beetroot juice nutrition",
            "Pomegranate juice nutrition", "Amla juice nutrition", "Lemon juice nutrition",
            "Watermelon juice nutrition", "Sugarcane juice nutrition"
        ],
        "🫘 Soya & Legumes": [
            "Soya bean nutrition", "Soya milk nutrition",
            "Tofu nutrition", "Soya chunks nutrition"
        ],
        "🌱 Sprouts": [
            "Moong sprouts nutrition", "Chickpea sprouts nutrition",
            "Wheat sprouts nutrition", "Fenugreek sprouts nutrition",
            "Lentil sprouts nutrition"
        ],
        "🌾 Millets": [
            "Ragi nutrition", "Bajra nutrition", "Jowar nutrition",
            "Foxtail millet nutrition", "Kodo millet nutrition",
            "Little millet nutrition"
        ],
        "🌾 Grains": [
            "Brown rice nutrition", "Quinoa nutrition", "Wheat nutrition",
            "Barley nutrition", "Corn nutrition", "Oats nutrition"
        ]
    }

    selected_items = food_map[category]
    for i, item in enumerate(selected_items):
        if st.button(item, key=f"cat_{category[:3]}_{i}"):
            st.session_state.messages.append({"role": "user", "text": item})
            response = get_response(item)
            st.session_state.messages.append({"role": "bot", "text": response})
            st.rerun()

    st.markdown("---")
    st.markdown("""
    <div class='disclaimer'>
    ⚠️ <b>Disclaimer:</b> MedEase is for informational purposes only. Always consult a qualified doctor.
    </div>
    """, unsafe_allow_html=True)

# ── Main Area ─────────────────────────────────────────────────
st.markdown("## 🌿 MedEase — AI Health Assistant")
st.caption("Ask me in English or Tamil | உங்கள் கேள்வியை தமிழிலும் கேட்கலாம்!")
st.markdown("---")

# ── Session State ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "bot",
            "text": (
                "Hello! I'm MedEase 🌿 Your personal AI health assistant.\n\n"
                "வணக்கம்! நான் MedEase. உங்கள் உடல் நலம் பற்றி கேளுங்கள்!\n\n"
                "You can ask me about symptoms, diet, BMI, fitness, or wellness tips!"
            )
        }
    ]

# ── Display Chat Messages ─────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-name-user'>You</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-bubble-user'>{msg['text']}</div>", unsafe_allow_html=True)
    else:
            if msg == st.session_state.messages[-1] and msg["role"] == "bot":
                container = st.empty()
                typed = ""
                for char in msg["text"]:
                    typed += char
                    container.markdown(
                        f"<div class='chat-name-bot'>🌿 MedEase</div><div class='chat-bubble-bot'>{typed.replace(chr(10), '<br>')}</div>",
                        unsafe_allow_html=True
                    )
                    time.sleep(0.01)
            else:
                st.markdown(
                    f"<div class='chat-bubble-bot'>{msg['text'].replace(chr(10), '<br>')}</div>",
                    unsafe_allow_html=True
                )
        

# ── Input Box ─────────────────────────────────────────────────
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            label="Your message",
            placeholder="Type your symptoms or health question here...",
            label_visibility="collapsed"
        )
    with col2:
        submitted = st.form_submit_button("Send ➤")

if submitted and user_input.strip():
    st.session_state.messages.append({"role": "user", "text": user_input})
    response = get_response(user_input)
    st.session_state.messages.append({"role": "bot", "text": response})

    # Show BMI gauge if BMI was calculated
    import re
    bmi_match = re.search(r'BMI\s*:\s*(\d+\.?\d*)', response)
    if bmi_match:
        bmi_val = float(bmi_match.group(1))
        st.session_state["last_bmi"] = bmi_val

    st.rerun()

# ── Clear Chat ────────────────────────────────────────────────
if len(st.session_state.messages) > 1:
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {"role": "bot", "text": "Hello again! How can I help you today? 🌿"}
        ]
        st.rerun()
if "last_bmi" in st.session_state:
    bmi = st.session_state["last_bmi"]
    st.markdown("### 📊 BMI Gauge")
    fill = min(int((bmi / 40) * 100), 100)
    color = "#1D9E75" if bmi < 25 else "#EF9F27" if bmi < 30 else "#E24B4A"
    st.markdown(f"""
    <div style='background:#eee; border-radius:10px; height:20px; width:100%;'>
        <div style='background:{color}; width:{fill}%; height:20px; border-radius:10px;'></div>
    </div>
    <p style='font-size:13px; color:{color}; font-weight:600;'>BMI: {bmi}</p>
    """, unsafe_allow_html=True)
