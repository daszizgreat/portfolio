import os
import base64
import streamlit as st

# Set page config
st.set_page_config(page_title="GDG Journey", layout="wide")

# Convert image to base64
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Local background image path
background_path = "pages/pictures/4853336.jpg"
background_image = get_base64(background_path)

# Inject background image CSS
st.markdown(f"""
    <style>
        .stApp {{
            background: url("data:image/jpg;base64,{background_image}") no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
""", unsafe_allow_html=True)

# Taskbar and styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Mate&display=swap');

        body {
            font-family: 'Mate', serif;
        }
            [data-testid="stSidebar"] {
            display: none;
        }

        .nav-button:hover {
            background: rgba(0,0,0);
            color: #000000;
            transform: scale(1.05);
        }

        .taskbar {
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
            margin-top: 20px;
            background: rgba(0, 0, 0, 0.65);
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

        .gdg-title {
            font-family: 'Mate', serif;
            font-size: 3.5rem;
            font-weight: 700;
            text-align: center;
            color: #000000;
            margin-top: 30px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
        }

        .section {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }

        .gdg-description {
            font-size: 1.2rem;
            color: #333;
            line-height: 2.7;
        }

        .gdg-image {
            width: 100%;
            max-width: 350px;
            display: block;
            margin: 0 auto;
            margin-top: 1rem;
        }

        .event-card {
            display: flex;
            flex-direction: row;
            gap: 20px;
            margin-top: 30px;
            background-color: rgba(240, 244, 248, 0.95);
            padding: 20px;
            border-radius: 12px;
            align-items: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        .event-card img {
            width: 180px;
            height: auto;
            border-radius: 8px;
            border: 3px solid #fff;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        }

        .event-content h3 {
            margin: 0;
            font-size: 1.5rem;
            color: #012a4a;
        }

        .event-content p {
            margin-top: 10px;
            font-size: 1rem;
            color: #444;
        }

        .event-content a {
            display: inline-block;
            margin-top: 10px;
            color: #1a73e8;
            text-decoration: none;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Taskbar HTML
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


# Title
st.markdown('<div class="gdg-title">Google Developer Group (GDG)</div>', unsafe_allow_html=True)

# Two-column layout
left, right = st.columns([2, 1])
with left:
    st.markdown("""
    <div class="section">
        <div class="gdg-description">
            <strong>GDG</strong> (Google Developer Groups) are global communities of developers and tech enthusiasts 
            who come together to explore and share knowledge around Google technologies and more. Whether online or offline, 
            GDGs foster collaboration, hands-on learning, and real-world impact.
        </div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="section" style="text-align:center;">
        <img src="https://developers.google.com/community/gdg/images/logo-lockup-gdg-horizontal_720.png" class="gdg-image" alt="GDG Logo">
        <a href="https://developers.google.com/community/gdg" target="_blank"><b>Visit GDG Official</b></a>
    </div>
    """, unsafe_allow_html=True)

# GDG Timeline Section
st.markdown('<div class="gdg-title" style="font-size:2.2rem; margin-top:50px;">My GDG Journey (2023 - 2025)</div>', unsafe_allow_html=True)

# 2023
st.markdown("""
<div class="event-card">
    <img src="https://cdn.qwiklabs.com/assets/leagues/silver_sm-64ca96b9e4cf1fc255fbe8e81fba4577965e8311.png" alt="GDG 2023 Badge">
    <div class="event-content">
        <h3>June 2023 – GDG Cloud Study Jam</h3>
        <p>My first exposure to hands-on Google Cloud labs, where I learned the foundations of cloud computing and participated in a global tech community.</p>
        <a href="https://www.cloudskillsboost.google/public_profiles/d5ddbe05-1272-4013-910f-da42de2a53ea" target="_blank">🔗 View 2023 Profile</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 2024
st.markdown("""
<div class="event-card">
    <img src="https://cdn.qwiklabs.com/assets/leagues/silver_sm-64ca96b9e4cf1fc255fbe8e81fba4577965e8311.png" alt="GDG 2024 Badge">
    <div class="event-content">
        <h3>October 2024 – GDG Silver League</h3>
        <p>Advanced to the Silver League by completing real-world labs, tackling intermediate GCP challenges, and actively contributing to community events.</p>
        <a href="https://www.cloudskillsboost.google/public_profiles/debaf5b8-8b2b-4dab-9135-d646c0c5e458" target="_blank">🔗 View 2024 Profile</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 2025
st.markdown("""
<div class="event-card">
    <img src="https://cdn.qwiklabs.com/assets/leagues/diamond_sm-6bb229d2803807410116694fb0aed7f6f43aa63a.png" alt="GDG 2025 Badge">
    <div class="event-content">
        <h3>May 2025 – GDG Diamond League</h3>
        <p>Reached the Diamond League with advanced cloud solutions, team-based collaboration projects, and leadership roles in GDG meetups.</p>
        <a href="https://www.cloudskillsboost.google/public_profiles/3b2f139f-68fa-4eb7-910b-61a51437a036" target="_blank">🔗 View 2025 Profile</a>
    </div>
</div>
""", unsafe_allow_html=True)
# SAE Club Title
st.markdown('<div class="gdg-title">Society of Automotive Engineers (SAE)</div>', unsafe_allow_html=True)

# Two-column layout for SAE
left_sae, right_sae = st.columns([2, 1])

with left_sae:
    st.markdown("""
    <div class="section">
        <div class="gdg-description">
            <strong>SAE</strong> is a global association of engineers and automotive enthusiasts committed to advancing mobility knowledge and solutions. 
            As a member, I participated in building, testing, and presenting real-world engineering projects, gaining hands-on experience in vehicle design and innovation.
        </div>
    </div>
    """, unsafe_allow_html=True)

with right_sae:
    st.markdown("""
    <div class="section" style="text-align:center;">
        <img src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRRfecPMRBvzHglLRf-T1ka7atx94sfGWJGvES8cTTnyTT81hLorS1EcZYLXYVL-VFZXdnPDC5pYA9KP6U_VdNHtBXFN1GqswuGcwSoeWnhlg" class="gdg-image" alt="SAE Logo">
        
    """, unsafe_allow_html=True)

# SAE Journey Heading
st.markdown('<div class="gdg-title" style="font-size:2.2rem; margin-top:50px;">My SAE Journey (2022 - 2025)</div>', unsafe_allow_html=True)

# SAE Event 1
st.image("pages/pictures/Aerothon.png", width=180)
st.markdown("""
<div class="event-card">
    <div class="event-content">
        <h3>Nov 2023 – Apr 2023 – Aerothon-2023</h3>
        <p>Contributed to Aerothon as part of a multidisciplinary team. Performed ANSYS simulations and MATLAB-based aerodynamic calculations. Designed and optimized payload structure and weight distribution. Integrated electronics for lighting systems, engine control, and propulsion.</p>
        
</div>
""", unsafe_allow_html=True)

# SAE Event 2
st.image("pages/pictures/ddc.png", width=180)
st.markdown("""
<div class="event-card">
    <div class="event-content">
        <h3>Aug 2023 – Jul 2024 – Drone Development Challenge</h3>
        <p>Played a core role in propulsion system design, motor selection, and thrust calculations. Simulated aerodynamic behavior using MATLAB and conducted load analysis for stability. Led construction and crafting of the drone body, integrating key electronics and wiring. Team advanced to final flight test rounds after successful structural and performance validation.</p>
        
</div>
""", unsafe_allow_html=True)

# SAE Event 3
st.image("pages/pictures/Aerothon.png", width=180)
st.markdown("""
<div class="event-card">
    <div class="event-content">
        <h3>Feb 2024 – Nov 2024 – Aerothon 2024</h3>
        <p>Focused on material selection and drone manufacturing enhancement.</p>
        
    
</div>
""", unsafe_allow_html=True)
