import streamlit as st
import base64
import os
import re
from dotenv import load_dotenv

# =========================================================
# 0. USE OFFICIAL GOOGLE SDK (No LangChain)
# =========================================================
try:
    import google.generativeai as genai
except ImportError:
    st.error("⚠️ Library Missing. Stop app and run: `pip install google-generativeai`")
    st.stop()

# Load environment variables
load_dotenv()

# =========================================================
# 1. CONFIG & HELPER FUNCTIONS
# =========================================================
st.set_page_config(
    page_title="PersonaLearn | Adaptive AI Tutor",
    page_icon="log.jpeg",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Routing State
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

def get_img_as_base64(file_path):
    """Converts image to base64 for HTML embedding"""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_path = "log.jpeg"
logo_b64 = get_img_as_base64(logo_path)

def switch_to_app():
    st.session_state.page = 'app'
    st.rerun()

def switch_to_landing():
    st.session_state.page = 'landing'
    st.rerun()

# =========================================================
# 2. LANDING PAGE VIEW
# =========================================================
def render_landing_page():
    st.markdown("""
    <style>
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: white; color: #0f172a; }
    header[data-testid="stHeader"] { display: none; }
    .block-container { padding-top: 90px !important; padding-bottom: 5rem !important; max_width: 100%; }
    .navbar { position: fixed; top: 0; left: 0; right: 0; height: 80px; background: white; border-bottom: 1px solid rgba(1,74,173,0.15); display: flex; align-items: center; justify-content: space-between; padding: 0 3rem; z-index: 99999; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    .nav-left { display: flex; align-items: center; gap: 12px; font-size: 1.5rem; font-weight: 800; color: #014aad; }
    .nav-logo-img { height: 45px; width: auto; }
    .nav-right a { margin-left: 2rem; text-decoration: none; color: #334155; font-weight: 600; font-size: 1rem; transition: color 0.2s; }
    .nav-right a:hover { color: #014aad; }
    .hero { padding: 5rem 3.5rem; border-radius: 24px; background: linear-gradient(135deg, rgba(1,74,173,0.05) 0%, rgba(1,74,173,0.01) 100%); margin-bottom: 4rem; }
    .hero h1 { font-size: 3.5rem; font-weight: 800; color: #014aad; line-height: 1.2; margin-bottom: 1.5rem; }
    .hero p { font-size: 1.25rem; max-width: 800px; color: #334155; line-height: 1.6; }
    .section-title { font-size: 2.2rem; font-weight: 800; color: #0f172a; margin-top: 4.5rem; margin-bottom: 1rem; }
    .card { padding: 2rem; border-radius: 18px; background: white; border: 1px solid #e2e8f0; height: 100%; transition: transform 0.2s; }
    .card:hover { transform: translateY(-5px); border-color: #014aad; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .card h3 { color: #014aad; font-weight: 700; margin-bottom: 0.8rem; }
    .try-now-container { margin-top: 5rem; padding: 4rem; border-radius: 26px; background: #014aad; color: white; text-align: center; background-image: radial-gradient(circle at top right, rgba(255,255,255,0.1), transparent); }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="navbar">
        <div class="nav-left"><img src="data:image/jpeg;base64,{logo_b64}" class="nav-logo-img"><span>PersonaLearn</span></div>
        <div class="nav-right"><a href="#features">Features</a><a href="#how">How It Works</a><a href="#impact">Impact</a><a href="#contact">Contact</a></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero"><h1>Learning, translated into your world with PersonaLearn.</h1><p>PersonaLearn is an adaptive AI tutor that reframes academic knowledge through the lens of a learner’s personal interests.</p></div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Why PersonaLearn Exists</div>', unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.1rem; color: #475569; max-width: 850px; margin-bottom: 2rem;'>Cognitive science shows that retention improves when new information is anchored to familiar mental models.</p>", unsafe_allow_html=True)

    st.markdown('<div id="features" class="section-title">Core Features</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    features = [("Interest Mapping", "Learners build a persistent interest profile."), ("Dynamic Translation", "Textbook concepts are reconstructed using analogies."), ("Quiz-to-Interest Mode", "Assessments are generated within the same interest context.")]
    for col, (t, d) in zip([c1, c2, c3], features):
        with col: st.markdown(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>', unsafe_allow_html=True)

    st.markdown('<div id="try" class="try-now-container"><h2>Experience learning that adapts to you.</h2><p style="font-size:1.1rem; margin-top:1rem; color: #e2e8f0; margin-bottom: 2rem;">No login. No setup. Step directly into PersonaLearn.</p>', unsafe_allow_html=True)
    col_spacer, col_btn, col_spacer2 = st.columns([1,1,1])
    with col_btn:
        if st.button("LAUNCH DEMO 🚀", type="primary", use_container_width=True):
            switch_to_app()
    st.markdown('</div><br><br><br>', unsafe_allow_html=True)

# =========================================================
# 3. APPLICATION VIEW
# =========================================================
def render_app_page():
    st.markdown("""
    <style>
        .block-container { padding-top: 2rem !important; }
        section[data-testid="stSidebar"] { background-color: #f8fafc; }
        .stButton>button { border-radius: 8px; height: 3em; background-color: #007BFF; color: white; font-weight: bold; border: none; }
        .stButton>button:hover { background-color: #0056b3; color: white; }
        div[data-testid="stMetricValue"] { font-size: 1.5rem; color: #007BFF; }
        .stCheckbox { background-color: #F0F8FF; padding: 8px; border-radius: 5px; margin-bottom: 5px; border: 1px solid #d1e7ff; }
        .carbon-card { background-color: #e6fffa; border: 1px solid #b2f5ea; padding: 15px; border-radius: 10px; margin-top: 10px; color: #234e52; }
    </style>
    """, unsafe_allow_html=True)

    # STATE
    DEFAULT_SYLLABI = {
        "School": ["Photosynthesis (Bio)", "Newton's Laws (Physics)", "Algebra Basics (Math)"],
        "SSC": ["Number System", "Reasoning Analogies", "General Awareness"],
        "UPSC": ["Indian Polity (Articles)", "Modern History (1857 Revolt)", "Geography (Monsoons)"],
        "General": ["Artificial Intelligence", "Climate Change", "Blockchain"]
    }
    if 'syllabus' not in st.session_state: st.session_state.syllabus = [{"topic": t, "completed": False} for t in DEFAULT_SYLLABI["UPSC"]]
    if 'user_score' not in st.session_state: st.session_state.user_score = 0
    if 'quiz_count' not in st.session_state: st.session_state.quiz_count = 0
    if 'last_token_count' not in st.session_state: st.session_state.last_token_count = 0
    if 'generated_quiz_data' not in st.session_state: st.session_state.generated_quiz_data = None
    if 'current_exam_mode' not in st.session_state: st.session_state.current_exam_mode = "UPSC"

    def check_ans(user_choice, data):
        if user_choice == data["correct"]:
            st.balloons(); st.success("Correct!"); st.session_state.user_score += 1
        else:
            st.error(f"Wrong. Correct was {data['correct']}")
        st.write(f"**Why?** {data['explain']}")
        st.session_state.quiz_count += 1

    api_key = os.getenv("GOOGLE_API_KEY")

    # SIDEBAR
    with st.sidebar:
        if st.button("⬅️ Back to Home", type="secondary"): switch_to_landing()
        st.divider(); st.image(logo_path, width=60); st.title("Settings")
        if not api_key:
            st.warning("⚠️ No Gemini API Key"); api_key = st.text_input("Enter Key", type="password")
        role_mode = st.radio("View Mode", ["Student 🎓", "Professor 👨‍🏫"], horizontal=True)
        st.divider()
        exam_type = st.selectbox("Target Exam", ["School", "SSC", "UPSC", "General"], index=2)
        if exam_type != st.session_state.current_exam_mode:
            st.session_state.current_exam_mode = exam_type
            st.session_state.syllabus = [{"topic": t, "completed": False} for t in DEFAULT_SYLLABI[exam_type]]
            st.rerun()
        interest = st.selectbox("Analogy Theme", ["Minecraft", "Cricket", "Marvel", "Cooking", "K-Pop"], index=1)
        st.markdown("### 🎛️ Output Controls")
        length_setting = st.select_slider("Length", options=["Short", "Medium", "Long"], value="Medium")
        level = st.select_slider("Complexity", options=["Basic", "Intermediate", "Advanced"], value="Intermediate")
        st.divider()
        if role_mode == "Student 🎓":
            c1, c2 = st.columns(2); c1.metric("Score", st.session_state.user_score); c2.metric("Quizzes", st.session_state.quiz_count)

    # MAIN
    col_head_logo, col_head_title = st.columns([1, 15])
    with col_head_logo: st.image(logo_path, width=60) 
    with col_head_title: st.subheader(f"PersonaLearn Pro: {exam_type} Edition"); st.caption("AI-Powered Adaptive Learning System")

    with st.expander("📝 Syllabus & Progress", expanded=False):
        if role_mode == "Professor 👨‍🏫":
            new_topic = st.text_input("Add Topic")
            if st.button("Add"):
                if new_topic: st.session_state.syllabus.append({"topic": new_topic, "completed": False}); st.rerun()
            for i, item in enumerate(st.session_state.syllabus):
                c_del, c_txt = st.columns([1, 10])
                if c_del.button("❌", key=f"d{i}"): st.session_state.syllabus.pop(i); st.rerun()
                c_txt.write(item["topic"])
        else:
            total = len(st.session_state.syllabus); done = sum(1 for t in st.session_state.syllabus if t["completed"])
            if total > 0: st.progress(done/total, text=f"{int(done/total*100)}% Completed")
            cols = st.columns(3)
            for i, item in enumerate(st.session_state.syllabus):
                with cols[i % 3]:
                    is_done = st.checkbox(item["topic"], value=item["completed"], key=f"c{i}")
                    st.session_state.syllabus[i]["completed"] = is_done
    st.divider()

    # --- NATIVE AI LOGIC ---
    if api_key:
        # CONFIGURE THE NATIVE LIBRARY
        genai.configure(api_key=api_key)
        
        # MODEL SELECTION (Prioritize Stable)
        model = None
        for m_name in ["gemini-2.5-flash", "gemini-pro"]:
            try:
                model = genai.GenerativeModel(m_name)
                break
            except: continue
            
        if not model: model = genai.GenerativeModel("gemini-pro") # Fallback

    else:
        st.error("Please enter API Key in sidebar")

    col_left, col_right = st.columns([1, 1.5], gap="medium")
    with col_left:
        st.subheader("📚 Input")
        user_text = st.text_area("Enter concept...", height=120)
        
        if st.button("🚀 Explain It!", type="primary"):
            if user_text and api_key:
                with st.spinner("Generating..."):
                    # RAW PROMPT CONSTRUCTION
                    prompt = f"""
                    Act as an expert educator for {exam_type}.
                    Explain: "{user_text}" using the analogy of "{interest}".
                    Level: {level}. Length: {length_setting}
                    Structure: 2 sentence summary followed by detailed explanation.
                    """
                    try:
                        response = model.generate_content(prompt)
                        st.session_state.translated_text = response.text
                        st.session_state.last_token_count = 500 # Approximate for native
                        st.session_state.generated_quiz_data = None
                        st.rerun()
                    except Exception as e:
                        st.error(f"AI Error: {e}")

    with col_right:
        st.subheader("💡 Output")
        if 'translated_text' in st.session_state and st.session_state.translated_text:
            with st.container(border=True):
                st.markdown(st.session_state.translated_text)
            
            st.divider()
            if st.button("❓ Take Quiz"):
                if api_key:
                    with st.spinner("Drafting question..."):
                        q_prompt = f"""
                        Based on this text: "{st.session_state.translated_text}"
                        Generate 1 Multiple Choice Question.
                        Strict Format:
                        Question: [Text]
                        A) [Option]
                        B) [Option]
                        C) [Option]
                        D) [Option]
                        Answer: [A/B/C/D]
                        Explanation: [Reason]
                        """
                        try:
                            q_res = model.generate_content(q_prompt).text
                            ans = re.search(r"Answer:\s*([A-D])", q_res, re.IGNORECASE)
                            st.session_state.generated_quiz_data = {
                                "text": q_res.split("Answer:")[0],
                                "correct": ans.group(1).upper() if ans else "A",
                                "explain": q_res.split("Explanation:")[-1] if "Explanation:" in q_res else ""
                            }
                            st.rerun()
                        except Exception as e: st.error(f"Quiz Error: {e}")

            if st.session_state.generated_quiz_data:
                data = st.session_state.generated_quiz_data
                st.info("📝 **Quick Check**")
                st.markdown(data["text"])
                c1, c2, c3, c4 = st.columns(4)
                if c1.button("A"): check_ans("A", data)
                if c2.button("B"): check_ans("B", data)
                if c3.button("C"): check_ans("C", data)
                if c4.button("D"): check_ans("D", data)

if st.session_state.page == 'landing': render_landing_page()
else: render_app_page()