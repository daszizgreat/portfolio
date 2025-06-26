import os
import base64
import streamlit as st

# Disable Streamlit file watcher error
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

# --- Set Page Config ---
st.set_page_config(layout="wide")
st.title("📚 Education")

# === Set Background ===
def get_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

background_image_path = "pages/pictures/bg.jpg"
img_base64 = get_base64(background_image_path)
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
# === CSS Styling ===
st.markdown(f"""
    <style>
            
        .stApp {{
            background: url("data:image/jpg;base64,{img_base64}") no-repeat center center fixed;
            background-size: cover;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }}
        
        .school-name {{
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
            color: black;
        }}
        h1, h2, h3, h4, h5, h6, p {{
            color: black !important;
        }}
        .block-container {{
            padding-top: 2rem;
        }}
    </style>
""", unsafe_allow_html=True)

# === Function to render each education card ===
def render_education(board, school, marks_or_cgpa, image_path, location, years):
    st.markdown("<div class='edu-box'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.subheader(school)
        st.markdown(f"**Board:** {board}")
        st.markdown(f"**Years:** {years}")
        st.markdown(marks_or_cgpa)
        st.markdown(f"📍 *{location}*")

    with col2:
        st.image(image_path, use_container_width=True)
        st.markdown(f"<div class='school-name'>{school}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# === Education Entries ===
render_education(
    board="ICSE Board",
    school="Methodist School",
    marks_or_cgpa="**Marks:** 83.5%",
    image_path="pages/pictures/methodist_school.png",
    location="Coal Complex Township, Dankuni, West Bengal 712310",
    years="2006 – 2020"
)

render_education(
    board="CBSE Board",
    school="Vivekananda Academy",
    marks_or_cgpa="**Marks:** 65.2%",
    image_path="pages/pictures/vivekananda_academy.png",
    location="Bhattacharjee Garden, Serampore, West Bengal 712203",
    years="2020 – 2022"
)

render_education(
    board="B.Tech in CSE (IoTCSBT)",
    school="Institute of Engineering and Management",
    marks_or_cgpa="**CGPA:** 8.77",
    image_path="pages/pictures/iem_kolkata.png",
    location="Sector V, Salt Lake, Kolkata, West Bengal 700091",
    years="2022 – 2026"
)
st.markdown("""
    <style>
       


        .nav-button:hover {
            background: rgba(0,0,0);
            color: #000000;
            transform: scale(1.05);
        }

        /* Taskbar buttons */
        .taskbar {
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
            margin-top: 20px;
            background: rgba(0, 0, 0);
            padding: 20px;
            border-radius: 20px;
            backdrop-filter: blur(12px);
            box-shadow: 0 8px 30px rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.15);
        }

        .taskbar a {
            text-decoration: none;
            padding: 12px 28px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            color: #e2e2e2;
            background: rgba(0,0,0,0.3);
            transition: all 0.25s ease;
            border: 1px solid rgba(255, 255, 255, 0.12);
        }

        .taskbar a:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)


# --- Taskbar with 7 Buttons ---
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