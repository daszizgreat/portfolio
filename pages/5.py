import os
import base64
import streamlit as st

# Prevent file watcher crash on Windows
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

# Page config
st.set_page_config(page_title="Projects & Tools", page_icon="🛠️", layout="wide")

# Load background image as base64
background_path = "pages/pictures/bg2.jpg"

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64(background_path)

# CSS styling
st.markdown(f"""
    <style>
        .stApp {{
            background: url("data:image/jpg;base64,{bg_img}") no-repeat center center fixed;
            background-size: cover;
            color: white;
        }}
        .card-left {{
            flex: 3;
            padding-right: 20px;
        }}
        .card-left h4 {{
            color: #ffffff;
            margin-bottom: 5px;
        }}
        .card-left p {{
            color: #1a1818;
            margin: 6px 0;
            font-size: 15px;
        }}
        .card-left a {{
            color: #4EA8F7;
            font-size: 14px;
            text-decoration: none;
        }}
        .card-left a:hover {{
            text-decoration: underline;
        }}
        .card-right {{
            flex: 1.2;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .project-image {{
            width: 400px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255,255,255,0.3);
        }}
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
st.title("🛠️ Projects & Tools")

# === Function to render a project block ===
def render_project(title, duration, description, github, image_path=None):
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1.2], gap="large")

    with col1:
        st.markdown(f"<div class='card-left'>", unsafe_allow_html=True)
        st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)
        st.markdown(f"<p><b>{duration}</b></p>", unsafe_allow_html=True)
        st.markdown(f"<p>{description}</p>", unsafe_allow_html=True)
        st.markdown(f"<a href='{github}' target='_blank'>🔗 View Project</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if image_path:
            try:
                with open(image_path, "rb") as img_file:
                    img_base64 = base64.b64encode(img_file.read()).decode()
                    st.markdown(f"""
                        <div class='card-right'>
                            <img src="data:image/png;base64,{img_base64}" class='project-image'>
                        </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f"<p style='color:red;'>⚠️ Could not load image: {image_path}</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# === Render project entries ===

render_project(
    title="Aerothon-2023",
    duration="Nov 2023 – Apr 2023",
    description="""Contributed to Aerothon as part of a multidisciplinary team.
Performed ANSYS simulations and MATLAB-based aerodynamic calculations.
Designed and optimized payload structure and weight distribution.
Integrated electronics for lighting systems, engine control, and propulsion.""",
    github="",
    image_path="pages/pictures/Aerothon.png"
)

render_project(
    title="Drone Development Challenge",
    duration="Aug 2023 – Jul 2024",
    description="""Played a core role in propulsion system design, motor selection, and thrust calculations.
Simulated aerodynamic behavior using MATLAB and conducted load analysis for stability.
Led construction and crafting of the drone body, integrating key electronics and wiring.
Team advanced to final flight test rounds after successful structural and performance validation.""",
    github="",
    image_path="pages/pictures/ddc.png"
)

render_project(
    title="Aerothon 2024",
    duration="Feb 2024 – Nov 2024",
    description="Focused on material selection and drone manufacturing enhancement.",
    github="",
    image_path="pages/pictures/Aerothon.png"
)

render_project(
    title="Online Grievance Redressal System",
    duration="Jan 2024 – Mar 2024",
    description="""Built a full-stack Online Grievance Redressal System aimed at streamlining citizen complaint management for public and institutional use. The platform includes secure sign-in/login functionality and allows users to file grievances with category tagging. It features real-time status tracking through the “Status Spotlight” module and offers options to connect with relevant authorities or support representatives. The “Behind the Cause” section educates users about their rights and complaint processes. An integrated chatbot provides instant support and guidance, enhancing user experience. Administrators and authority figures access a separate login panel for secure response handling. Users can also lodge appeals for unresolved issues, maintaining transparency. Buyer and seller data management modules were implemented to ensure proper tracking of cases in commercial or service-related contexts. The system is built using Python, Streamlit, and MongoDB, offering an intuitive interface and scalable backend.""",
    github="https://github.com/daszizgreat/Online-grevience-readressal-system",
    image_path="pages/pictures/orgs.png"
)

render_project(
    title="MyTeacher AId",
    duration="Ongoing",
    description="""Developed a comprehensive AI-powered productivity suite using Streamlit and advanced language models (Gemini/OpenAI), designed to streamline content generation tasks. The toolkit includes modules for generating emails, formal letters, notices, and messages, each tailored for professional communication. It also features a Minutes of Meeting Generator that summarizes discussions into actionable insights, a Grammar Checker to identify and correct linguistic errors, and a Word Generator for vocabulary enhancement. Additionally, the suite offers a Text Summarizer for condensing long content and a Paraphrasing tool to rephrase text while preserving meaning. The application is modular, lightweight, and optimized for both educators and professionals, delivering quick, reliable outputs via an intuitive interface. The entire suite can run locally or as a deployable web app, supporting a wide range of academic and organizational tasks.""",
    github="https://github.com/daszizgreat/Teacher-helper-app",
    image_path="pages/pictures/teacher.png"
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
            background: rgba(255, 255, 255);
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