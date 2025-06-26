import streamlit as st
import base64

# --- Page Configuration ---
st.set_page_config(page_title="My Skills", layout="wide")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Load & Encode Background Image ---
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

image_path = "pages/pictures/4853433.jpg"
img_base64 = get_base64(image_path)

# --- Custom CSS Styling ---
st.markdown(f"""
    <style>
        .stApp {{
            background: url("data:image/jpg;base64,{img_base64}") no-repeat center center fixed;
            background-size: cover;
            font-family: 'Segoe UI', sans-serif;
            width: 100%;
            max-width: none;
        }}

        .taskbar {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 16px;
            margin: 0 auto 20px;
            padding: 20px;
            border-radius: 20px;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            box-shadow: 0 8px 30px rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.15);
            max-width: 100%;
        }}

        .taskbar a {{
            text-decoration: none;
            padding: 12px 28px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            color: #e2e2e2;
            background: rgba(0, 0, 0, 0.3);
            transition: all 0.25s ease;
            border: 1px solid rgba(255, 255, 255, 0.12);
        }}

        .taskbar a:hover {{
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
        }}

        h1 {{
            text-align: center;
            font-size: 3rem;
            color: #0f172a;
            margin-bottom: 3rem;
        }}

        h1 span {{
            color: #3b82f6;
        }}

        .section-title {{
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            color: #0f172a;
        }}

        .skill-card {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 16px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.04);
        }}

        .skill-name {{
            font-size: 1.1rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 10px;
        }}

        .progress-container {{
            width: 100%;
            background: #cbd5e1;
            border-radius: 12px;
            height: 12px;
            position: relative;
            overflow: hidden;
        }}

        .progress-bar {{
            height: 100%;
            border-radius: 12px;
            background: linear-gradient(90deg, #3b82f6, #06b6d4);
            transition: width 0.5s ease-in-out;
        }}

        .percent-label {{
            position: absolute;
            right: 10px;
            top: -22px;
            font-weight: 500;
            color: #475569;
            font-size: 12px;
        }}

        .soft-skill {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 12px;
            padding: 14px 20px;
            margin: 10px;
            font-weight: 600;
            color: #334155;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            font-size: 1rem;
        }}
    </style>
""", unsafe_allow_html=True)

# --- Navigation Buttons ---
st.markdown("""
<div class="taskbar">
    <a href="/">🏠 Home</a>
    <a href="/3" target="_self">🎓 Education</a>
    <a href="/2" target="_self">🛠️ Skills</a>
    <a href="/5" target="_self">🚀 Projects</a>
    <a href="/6" target="_self">📜 Certificates</a>
    <a href="/1" target="_self">🎯 Clubs</a>
    <a href="/4" target="_self">💼 Internship</a>
</div>
""", unsafe_allow_html=True)

# --- Page Title ---
st.markdown("<h1>🚀 My <span>Skills</span></h1>", unsafe_allow_html=True)

# --- Hard Skills ---
st.markdown('<div class="section-title">🔧 Hard Skills</div>', unsafe_allow_html=True)
skills = {
    "C 🧠": 80, "Python 🐍": 90, "CSS 🎨": 85, "Streamlit 🌟": 85,
    "Git 🗂️": 80, "MongoDB 🍃": 75, "SQL 🗃️": 80, "ANSYS 🗃️": 80
}
cols = st.columns(4)
for i, (skill, percent) in enumerate(skills.items()):
    with cols[i % 4]:
        st.markdown(f"""
            <div class="skill-card">
                <div class="skill-name">{skill}</div>
                <div class="progress-container">
                    <div class="progress-bar" style="width: {percent}%;"></div>
                    <div class="percent-label">{percent}%</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- Soft Skills ---
st.markdown('<div class="section-title">🌟 Soft Skills</div>', unsafe_allow_html=True)
soft_skills = [
    "Productive", "Problem-solving", "Teamwork skills", 
    "Creativity", "Leadership", "Adaptability"
]
soft_cols = st.columns(3)
for i, skill in enumerate(soft_skills):
    with soft_cols[i % 3]:
        st.markdown(f'<div class="soft-skill">{skill}</div>', unsafe_allow_html=True)

# --- Tools & Frameworks ---
st.markdown('<div class="section-title">🧰 Tools & Frameworks</div>', unsafe_allow_html=True)
tools = ["Jupyter", "Visual Studio"]
tool_cols = st.columns(2)
for i, tool in enumerate(tools):
    with tool_cols[i % 2]:
        st.markdown(f'<div class="soft-skill">{tool}</div>', unsafe_allow_html=True)

# --- Operating Systems ---
st.markdown('<div class="section-title">💻 Operating Systems</div>', unsafe_allow_html=True)
oses = ["Windows", "Linux"]
os_cols = st.columns(2)
for i, os in enumerate(oses):
    with os_cols[i % 2]:
        st.markdown(f'<div class="soft-skill">{os}</div>', unsafe_allow_html=True)
