import os
import base64
import streamlit as st

# === Config ===
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
st.set_page_config(layout="wide", page_title="Internship & Contact", page_icon="📞")

st.title("💼 Internship ")

# === Background Utility ===
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

background_path = "pages/pictures/4853433.jpg"
img_base64 = get_base64(background_path)

# === CSS ===
st.markdown(f"""
    <style>
        .stApp {{
            background: url("data:image/jpg;base64,{img_base64}") no-repeat center center fixed;
            background-size: cover;
        }}
        * {{
            color: #000 !important;
        }}
        .content-box {{
            background-color: rgba(255, 255, 255, 0.92);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(255, 255, 255, 0.92);
            width: 100%;
            max-width: 700px;
            margin: 40px auto;
            font-size: 16px;
        }}
        .content-box h3 {{
            text-align: center;
            margin-bottom: 20px;
            color: #000;
        }}
        .content-box p {{
            margin: 10px 0;
            line-height: 1.7;
            color: #000;
        }}
        .content-box a {{
            color: #000 !important;
            text-decoration: underline;
        }}
        .content-box a:hover {{
            color: #333;
        }}
        .bottom-link {{
            margin-top: 30px;
            text-align: center;
        }}
    </style>
""", unsafe_allow_html=True)

# === Hide Sidebar ===
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# === Internship Section ===
st.markdown("""
    <div class="content-box">
        <h3>💼 Internship at Aspireit (May 2024 – Aug 2024)</h3>
        <p>
        I recently completed an internship at Aspireit as part of the Founder’s Office from 28th May to 28th June 2024.
        During my time there, I actively participated in interview processes, presented app features to campus ambassadors,
        and supported marketing interns. I took ownership of tasks in the absence of leadership, created engaging presentations,
        and managed community interactions. I also helped maintain team communication and contributed significantly to 
        internal coordination and outreach. This experience helped strengthen my leadership, marketing, and communication skills.
        </p>
    </div>
""", unsafe_allow_html=True)

# === LeetCode Progress Section ===
st.markdown("""
    <div class="content-box">
        <h3>🧠 LeetCode Progress</h3>
        <p>
        I'm currently on my <strong>120th problem</strong> on LeetCode, actively improving my data structures and algorithm skills.
        You can view my latest progress and submissions at:
        <br>
        <a href="https://leetcode.com/u/soumyadeepdas2511/" target="_blank">
            🔗 leetcode.com/u/soumyadeepdas2511/
        </a>
        </p>
    </div>
""", unsafe_allow_html=True)

# === Contact Section ===
st.markdown("""
    <div class="content-box">
        <h3>📞 Let's Connect</h3>
        <p><strong>📍 Address:</strong> B-214, Dankuni Coal Complex Township, Hooghly, West Bengal – 712310</p>
        <p><strong>📧 Email:</strong> <a href="mailto:soumyadeepdas2511@gmail.com">soumyadeepdas2511@gmail.com</a></p>
        <p><strong>📱 Phone:</strong> <a href="tel:+918420124463">+91 84201 24463</a></p>
        <p><strong>🔗 LinkedIn:</strong> <a href="https://www.linkedin.com/in/soumyadeep-das-11717b239" target="_blank">soumyadeep-das-11717b239</a></p>
        <p><strong>🐙 GitHub:</strong> <a href="https://github.com/daszizgreat" target="_blank">github.com/daszizgreat</a></p>
        <div class="bottom-link">
            <a href="/5" target="_self">👉 Continue to Next Page</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# === Taskbar ===
st.markdown("""
    <style>
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
