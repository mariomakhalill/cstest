import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime

# ---------------------- Page Configuration ----------------------
st.set_page_config(
    page_title="CyberSec Portal",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# ---------------------- CSS Style ----------------------
st.markdown("""
    <style>
        .main { background-color: #0f1117; color: white; }
        .block-container { padding: 2rem; }
        h1, h2, h3, h4 { color: #61dafb; }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 16px;
            padding: 10px;
            margin: 0px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Header ----------------------
st.markdown("## 🛡️ CyberSecurity Community Portal")
st.markdown("Welcome to the interactive portal designed for the infosec community. Explore tools, share intelligence, and stay informed.")

# ---------------------- Tabs ----------------------
tabs = st.tabs(["🏠 Home", "🧰 Tools", "📰 Publish News", "📡 Threat Feeds", "ℹ️ About"])

# ---------------------- Home ----------------------
with tabs[0]:
    st.subheader("👋 Welcome")
    st.info("This platform is created to empower cybersecurity professionals, analysts, and enthusiasts.")
    st.success("🎯 Explore tabs above to access tools, feeds, and contribute your own insights.")

# ---------------------- Tools ----------------------
with tabs[1]:
    st.subheader("🧰 Open Source Intelligence Tools")
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 🔍 Domain Lookup")
        domain = st.text_input("Enter a domain (e.g. example.com)")
        if st.button("Scan Domain"):
            st.info(f"Scanned: {domain}")
            # Simulate result
            st.code("No malicious activity found.")
    
    with col2:
        st.write("### 💣 Malware Hash Checker")
        hash_input = st.text_input("Enter file hash (SHA256)")
        if st.button("Check Hash"):
            st.warning("🔍 This hash appears in multiple threat intel sources.")

# ---------------------- News Publisher ----------------------
with tabs[2]:
    st.subheader("📰 Publish Cybersecurity News")
    with st.form("news_form", clear_on_submit=True):
        title = st.text_input("News Title")
        author = st.text_input("Your Name")
        content = st.text_area("News Content")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        submitted = st.form_submit_button("Publish")
        if submitted:
            st.success("✅ News published successfully!")
            st.markdown(f"### {title}")
            st.markdown(f"**By:** {author}  \n📅 {date}")
            st.markdown(content)

# ---------------------- Threat Feeds ----------------------
with tabs[3]:
    st.subheader("📡 Live Threat Feeds (Demo)")
    st.info("Below are sample IOCs and feeds that will be auto-updated in future version.")
    st.table({
        "Type": ["Phishing Domain", "Malicious IP", "Fake App Hash"],
        "Value": ["login-secure-fb.com", "185.220.101.34", "9f8a3b2...e4f2c1"],
        "Source": ["Internal DB", "Abuse.ch", "VT"]
    })

# ---------------------- About ----------------------
with tabs[4]:
    st.subheader("ℹ️ About This Portal")
    st.markdown("""
    - Built with ❤️ for the cybersecurity community
    - Hosted on GitHub
    - Allows quick access to tools, threat data, and user contributions
    - Future updates: API feeds, malware sandbox integrations, scam navigator, more

    **Maintainer:** `@yourname`  
    [GitHub Repo](https://github.com/yourusername/cybersec-portal)
    """)

# ---------------------- Footer ----------------------
st.markdown("---")
st.markdown("© 2025 | CyberSec Portal | Built with Streamlit")
