import streamlit as st
import time
from crew_setup import run_analysis, run_recommendation, run_price_hunt

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AI Product Recommandation Agent",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- MODERN LIGHT THEME CSS ---
st.markdown("""
    <style>
    /* Main Background - Soft White/Blue Gradient */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        color: #333333;
    }
    
    /* Chat Bubbles - White cards with soft shadows */
    .stChatMessage {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        color: #333333;
    }
    
    /* User Input Area */
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #333333;
        border-radius: 20px;
        border: 2px solid #e0e0e0;
        padding: 10px 15px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #3a7bd5;
        box-shadow: 0 0 0 2px rgba(58, 123, 213, 0.2);
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        color: #1a1a1a;
        background: -webkit-linear-gradient(45deg, #2b5876, #4e4376);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #2b5876 0%, #4e4376 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.6rem 2.5rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(43, 88, 118, 0.3);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(43, 88, 118, 0.4);
    }
    
    /* Status/Expander Box styling */
    .stStatusWidget {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
col1, col2 = st.columns([1, 12])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=60)
with col2:
    st.title("AI Shopping Assistant")
    st.caption("Powered by Multi-Agent CrewAI • Analyst • Recommender • Price Hunter")

st.divider()

# --- SESSION STATE INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your AI Shopping Assistant. Tell me what you're looking for, and my team of agents will help you find the best deal."}
    ]
if "current_step" not in st.session_state:
    st.session_state.current_step = 0  # 0: Idle, 1: Profile Ready, 2: Products Ready

# --- DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- AGENT LOGIC HANDLERS ---

def handle_analysis(user_input):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Agent 1: Analyst
    with st.chat_message("assistant"):
        with st.status("🕵️‍♂️ Analyst Agent is working...", expanded=True) as status:
            st.write("Analyzing your needs...")
            time.sleep(1)
            st.write("Building shopper profile...")
            profile = run_analysis(user_input)
            status.update(label="✅ Profile Created", state="complete", expanded=False)
        
        response_text = f"**I've analyzed your request.** Here is the profile I built for you:\n\n{profile}"
        st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
        # Save profile for next step
        st.session_state.last_profile = profile
        st.session_state.current_step = 1
        st.rerun()

def handle_recommendation():
    with st.chat_message("assistant"):
        with st.status("🛍️ Recommender Agent is searching...", expanded=True) as status:
            st.write("Consulting product database...")
            time.sleep(1)
            st.write("Selecting top 3 matches...")
            recommendations = run_recommendation(st.session_state.last_profile)
            status.update(label="✅ Recommendations Found", state="complete", expanded=False)
        
        response_text = f"**Here are my top picks for you:**\n\n{recommendations}"
        st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
        # Save recommendations for next step
        st.session_state.last_recs = recommendations
        st.session_state.current_step = 2
        st.rerun()

def handle_price_hunt():
    with st.chat_message("assistant"):
        with st.status("💰 Price Hunter is finding deals...", expanded=True) as status:
            st.write("Scouring online stores...")
            time.sleep(1)
            st.write("Generating direct links...")
            prices = run_price_hunt(st.session_state.last_recs)
            status.update(label="✅ Prices & Links Found", state="complete", expanded=False)
        
        response_text = f"**I found the best prices and links for you:**\n\n{prices}"
        st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
        # Reset step to allow new search
        st.session_state.current_step = 0 

# --- USER INPUT HANDLING ---

# If we are in Step 0 (Waiting for initial input)
if st.session_state.current_step == 0:
    user_input = st.chat_input("e.g., I need a lightweight laptop for coding under $1000...")
    if user_input:
        handle_analysis(user_input)

# If we are in Step 1 (Profile Ready -> Waiting for user approval to Recommend)
elif st.session_state.current_step == 1:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Find Products Matching This Profile"):
            handle_recommendation()
    with col2:
        if st.button("❌ Cancel / Start Over"):
            st.session_state.current_step = 0
            st.rerun()

# If we are in Step 2 (Products Ready -> Waiting for user approval to Find Prices)
elif st.session_state.current_step == 2:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💸 Find Best Prices & Links"):
            handle_price_hunt()
    with col2:
        if st.button("🔄 Start New Search"):
            st.session_state.current_step = 0
            st.rerun()
