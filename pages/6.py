import streamlit as st

# Page configuration
st.set_page_config(page_title="🎓 Certifications & Achievements", layout="wide")
st.title("🏅 Certifications & Achievements")

# --- Custom CSS for Glassmorphism ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #232526, #414345);
        }
        .glass-box {
            background: rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.3);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        .glass-box a {
            color: #a8d0e6;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
        }
        .glass-box a:hover {
            text-decoration: underline;
        }
        .section-heading {
            font-size: 20px;
            font-weight: bold;
            color: #000000;
            margin-top: 20px;
        }
        .highlight {
            font-size: 17px;
            color: #000000;
            background-color: rgba(255, 255, 255, 0.05);
            padding: 15px;
            margin-top: 20px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Certificate Data
certificates = [
    ("Hands-on Internet of Things", "https://www.coursera.org/account/accomplishments/specialization/WU3MVBCT4MDB"),
    ("Programming Fundamentals", "https://www.coursera.org/account/accomplishments/verify/6CKG36HKZ6Z7"),
    ("Introduction to Artificial Intelligence (AI)", "https://www.coursera.org/account/accomplishments/verify/DCUZV6X7FZD4"),
    ("Cyber Attack Countermeasures", "https://www.coursera.org/account/accomplishments/verify/2WBPQPCW4BJT"),
    ("Capstone: Retrieving, Processing, and Visualizing Data with Python", "https://www.coursera.org/account/accomplishments/verify/QMXHJS7WZ6VS"),
    ("IoT Devices", "https://www.coursera.org/account/accomplishments/verify/89H37MXJ3UY5"),
    ("Machine Learning for All", "https://www.coursera.org/account/accomplishments/verify/TUQHM3HH94YY"),
    ("IoT Cloud", "https://www.coursera.org/account/accomplishments/verify/33JEM83YDC64"),
    ("IoT Communications", "https://www.coursera.org/account/accomplishments/verify/WDZJAS9YWQ7U"),
    ("IoT Networking", "https://www.coursera.org/account/accomplishments/verify/CQNQPF8BSZAU"),
    ("C for Everyone: Programming Fundamentals", "https://www.coursera.org/account/accomplishments/verify/V2N59HX5K4EH"),
    ("Introduction to Cyber Attacks", "https://www.coursera.org/account/accomplishments/verify/L87YHGNBB9XT"),
    ("Using Python to Access Web Data", "https://www.coursera.org/account/accomplishments/verify/S58RFC4PQK4C"),
    ("Python Data Structures", "https://www.coursera.org/account/accomplishments/verify/YNU7H7DN8HTJ"),
    ("Programming for Everybody (Getting Started with Python)", "https://www.coursera.org/account/accomplishments/verify/STV5Y4F95L6W"),
]

# Render Certificate Glass Box
st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>📜 Coursera Certifications</div>", unsafe_allow_html=True)

for name, link in certificates:
    st.markdown(f"<a href='{link}' target='_blank'>🔗 {name}</a>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Additional Achievements Section
st.markdown("""
    <div class='glass-box'>
        <div class='section-heading'>🏆 Additional Achievements</div>
        <div class='highlight'>
            🥈 Secured <b>2nd place</b> at <b>HackOasis</b>, building a real-time AI+IoT-based smart automation solution.<br><br>
            🌱 Made significant contributions during <b>Google Summer of Code</b> (GSoC) in the domain of AI-powered accessibility tools.
        </div>
    </div>
""", unsafe_allow_html=True)
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
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
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