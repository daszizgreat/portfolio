import streamlit as st
import os
import base64

# --- Page Config ---
st.set_page_config(page_title="Soumyadeep CV", layout="wide")

# --- File Paths ---
video_path = r"pages/pictures/rainy-forest.3840x2160.mp4"
pic_path = r"pages/pictures/1741947895373.jpg"

# --- Convert to Base64 ---
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_b64 = get_base64(pic_path) if os.path.exists(pic_path) else ""
video_b64 = get_base64(video_path) if os.path.exists(video_path) else ""

# --- CSS ---
st.markdown("""
    <style>
            [data-testid="stSidebar"] {
            display: none;
        }
        .container {
            display: flex;
            height: 100vh;
            overflow: hidden;
        }
        .left {
            flex: 1;
            position: relative;
        }
        .left video {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .left img {
            position: absolute;
            top: 60%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            height: 300px;
            border: 5px solid white;
            object-fit: cover;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.6);
        }

        .right {
            flex: 1;
            background: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }
        .name {
            font-size: 3rem;
            font-weight: bold;
            color: #012a4a;
        }
        .desc {
            margin-top: 10px;
            font-size: 1.2rem;
            color: #444;
            text-align: center;
        }
        .btn {
            margin-top: 20px;
            background-color: #012a4a;
            color: white;
            padding: 12px 24px;
            font-size: 1rem;
            border-radius: 25px;
            border: none;
            cursor: pointer;
        }
        .social {
            margin-top: 30px;
            display: flex;
            gap: 20px;
        }
        .social a img {
            width: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# --- HTML Layout ---
if video_b64 and img_b64:
    st.markdown(f"""
    <div class="container">
        <div class="left">
            <video autoplay muted loop>
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            </video>
            <img src="data:image/jpeg;base64,{img_b64}" alt="Profile Picture">
        </div>
        <div class="right">
            <div class="name">Soumyadeep Das</div>
            <div class="desc">Enthusiastic CSE student with a strong foundation in
programming, problem-solving, and teamwork. Proactive, detail-oriented, and committed to continuous learning and technology innovation.
</div>
            <div class="social">
                <a href="https://github.com/daszizgreat"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" /></a>
                <a href="https://www.linkedin.com/in/soumyadeep-das-11717b239/"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" /></a>
                <a href="https://leetcode.com/u/soumyadeepdas2511/"><img src="https://cdn-icons-png.flaticon.com/512/733/733635.png" /></a>
                <a href="https://www.instagram.com/daszz_is_great/"><img src="https://cdn-icons-png.flaticon.com/512/1384/1384031.png" /></a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.error("Image or video file not found.")
# --- Custom CSS ---
st.markdown("""
    <style>
        /* Page background */
        .stApp {
            background: linear-gradient(135deg, #1f1f1f, #2b2b2b);
            font-family: 'Segoe UI', sans-serif;
        }


        .nav-button:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #ffffff;
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
