
import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# --- 1. INITIALIZATION & CONFIG ---
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
# Using the Llama 3.3 model as per your requirements
langchain_llm = ChatGroq(api_key=groq_api_key, model="llama-3.3-70b-versatile")

st.set_page_config(page_title="Zenith AI Fitness", layout="wide", page_icon="🧘‍♀️")

# Premium Glassmorphism CSS for a 2026 "Pro" Feel
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp { 
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); 
        color: white; 
    }
    
    /* Glass Effect Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }

    /* Modern Buttons */
    div.stButton > button { 
        background-color: #00d2ff; 
        color: white; 
        border-radius: 12px; 
        border: none;
        padding: 10px 24px; 
        transition: all 0.3s ease; 
        font-weight: bold; 
        width: 100%;
    }
    
    div.stButton > button:hover { 
        background-color: #3a7bd5; 
        transform: translateY(-2px); 
        box-shadow: 0 5px 15px rgba(0, 210, 255, 0.4); 
    }

    /* Scrollable Output Container */
    .scrollable-response {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 15px;
        padding: 20px;
        max-height: 600px;
        overflow-y: auto;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Sidebar and Input Tweaks */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
    }
    
    h1, h2, h3 { color: #00d2ff !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. ADVANCED PROMPT TEMPLATES ---

plan_template = """
You are Zenith AI, a world-class fitness coach. Create a {number_of_weeks}-week diet and workout plan.
User Profile: {age}yo {gender}, {current_weight}kg (Target: {target_weight}kg).
Goal: {workout_type}. Diet: {diet_type}. Restrictions: {dietary_restrictions}.
Health Conditions: {health_conditions}. 
Instructions: {comments}.
Format: Professional Markdown tables for both Diet and Workout.
"""

pivot_template = """
Current Plan: {current_plan}. 
The user is currently feeling: {status_update}. 
Adapt the plan instantly. If 'Exhausted', provide a Deload/Recovery session. 
If 'Plateaued', increase intensity or adjust caloric intake.
Return only the modified today's plan.
"""

swap_template = """
Based on the plan: {current_plan}.
The user wants to swap: {meal_to_swap}.
Find a macro-equivalent alternative that fits the {diet_type} profile.
"""

omni_template = """
Original Workout: {current_plan}.
Environment: {mode}. Equipment: {equipment}.
Adjust today's workout to fit these constraints without losing the intended intensity.
"""

# --- 3. SESSION STATE MANAGEMENT ---
if "plan" not in st.session_state: st.session_state.plan = None
if "messages" not in st.session_state: st.session_state.messages = []
if "daily_update" not in st.session_state: st.session_state.daily_update = None

# --- 4. SIDEBAR & INPUTS ---
# --- 4. SIDEBAR & INPUTS (GLOBAL OPTIONS ENABLED) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/mountain.png", width=80)
    st.title("Zenith Settings")
    
    with st.expander("👤 User Profile", expanded=True):
        age = st.number_input("Age", 10, 100, 25)
        gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Other"])
        cur_w = st.number_input("Current Weight (kg)", 30.0, 250.0, 70.0)
        tar_w = st.number_input("Target Weight (kg)", 30.0, 250.0, 65.0)

    with st.expander("🥗 Diet & Workout Strategy"):
        # Expanded Goal Selection
        w_type = st.selectbox(
            "Workout Goal", 
            ["Weight Loss", "Muscle Gain", "Body Recomposition", "Functional Strength", "Endurance", "Flexibility"]
        )
        
        # Added Indian Vegetarian and regional options
        d_type = st.selectbox(
            "Dietary Theme", 
            [
                "Indian Vegetarian", 
                "Indian Non-Vegetarian", 
                "Mediterranean", 
                "Standard Western", 
                "Keto / Low-Carb", 
                "Vegan", 
                "Paleo", 
                "High Protein"
            ]
        )
        
        # Multiselect for specific cultural or health restrictions
        restr = st.multiselect(
            "Restrictions / Preferences",
            [
                "None", "Eggitarian", "Dairy-Free", "Gluten-Free", 
                "No Red Meat", "No Pork", "No Seafood", "Jain Diet", 
                "Low Sugar", "Peanut Allergy"
            ],
            default=["None"]
        )
        
        health = st.text_input("Medical Conditions", "None")
        weeks = st.slider("Plan Duration (Weeks)", 1, 12, 4)
        notes = st.text_area("Specific Instructions (e.g. 'I prefer North Indian food', 'Only 45 min workouts')")

    if st.button("🚀 Generate Zenith Plan"):
        st.session_state.messages = []
        restriction_str = ", ".join(restr)
        
        with st.spinner("Zenith is constructing your cultural and fitness blueprint..."):
            try:
                chain = LLMChain(llm=langchain_llm, prompt=PromptTemplate.from_template(plan_template))
                response = chain.run(
                    number_of_weeks=weeks, 
                    age=age, 
                    gender=gender, 
                    current_weight=cur_w,
                    target_weight=tar_w, 
                    workout_type=w_type, 
                    diet_type=d_type,
                    dietary_restrictions=restriction_str, 
                    health_conditions=health, 
                    comments=notes
                )
                st.session_state.plan = response
                st.success("Custom Plan Generated!")
            except Exception as e:
                st.error(f"Error connecting to Zenith: {e}")

# --- 5. MAIN UI ---
st.title("🏔️ Zenith AI Fitness Companion")

if st.session_state.plan:
    col1, col2 = st.columns([1, 1.5], gap="large")

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🏢 Omnichannel Training")
        mode = st.radio("Current Setting", ["Commercial Gym", "Home / Hotel"])

        # Replaced text_input with a multiselect dropdown
        equip_list = st.multiselect(
            "Available Gear", 
            options=[
                "Bodyweight Only", "Dumbbells", "Resistance Bands", 
                "Kettlebells", "Pull-up Bar", "Yoga Mat", 
                "Barbell", "Jump Rope", "Medicine Ball"
            ],
            default=["Bodyweight Only"]
        )

        # Convert the list to a string so the prompt can read it
        equip_str = ", ".join(equip_list)

        if st.button("Sync Workout Environment"):
            omni_chain = LLMChain(llm=langchain_llm, prompt=PromptTemplate.from_template(omni_template))
            # Pass the converted string (equip_str) to the chain
            st.session_state.daily_update = omni_chain.run(
                current_plan=st.session_state.plan, 
                mode=mode, 
                equipment=equip_str
            )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        tab1, tab2 = st.tabs(["📅 Master Plan", "🔄 Daily Adjustments"])
        
        with tab1:
            st.markdown(f'<div class="scrollable-response">{st.session_state.plan}</div>', unsafe_allow_html=True)
        
        with tab2:
            if st.session_state.daily_update:
                st.info("AI Adjustment Active")
                st.markdown(st.session_state.daily_update)
            else:
                st.write("No adjustments made yet. Use the Autopilot or Omnichannel tools.")

            st.markdown("---")
            st.subheader("🥪 Smart Meal Swap")
            meal = st.text_input("Meal to swap?", placeholder="e.g. Tuesday Lunch")
            if st.button("Find Equivalent"):
                swap_chain = LLMChain(llm=langchain_llm, prompt=PromptTemplate.from_template(swap_template))
                res = swap_chain.run(current_plan=st.session_state.plan, meal_to_swap=meal, diet_type=d_type)
                st.success(res)

    # --- CHAT SECTION ---

else:
    st.info("👈 Fill in your details in the sidebar to reach your Zenith.")

st.markdown("---")
st.caption("Zenith AI | Engineered for Peak Performance")


