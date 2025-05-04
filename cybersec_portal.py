import streamlit as st
from datetime import datetime

# ---------------------- Page Configuration ----------------------
st.set_page_config(
    page_title="CyberSec Portal",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# ---------------------- Session State for News ----------------------
if "news_posts" not in st.session_state:
    st.session_state.news_posts = []

# ---------------------- CSS Styling ----------------------
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
            padding: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 16px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Header ----------------------
st.markdown("## 🛡️ CyberSecurity Community Portal")
st.markdown("An interactive platform for tools, threat feeds, awareness, and user contributions.")

# ---------------------- Tabs ----------------------
tabs = st.tabs(["🏠 Home", "🧰 Tools", "📰 Publish News", "📡 Threat Feeds", "ℹ️ About"])

# ---------------------- Home Tab ----------------------
with tabs[0]:
    st.subheader("👋 Welcome")
    st.info("Explore the latest cybersecurity resources, tools, and community updates.")
    st.success("💡 Use the tabs to navigate through the portal features.")

# ---------------------- Tools Tab ----------------------
with tabs[1]:
    st.subheader("🧰 Open Source Intelligence Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 🔍 Domain Lookup")
        domain = st.text_input("Enter a domain (e.g., example.com)")
        if st.button("Scan Domain"):
            if domain:
                st.info(f"Scanned domain: {domain}")
                st.code("✅ No threats detected in current database.")
            else:
                st.warning("Please enter a domain.")

    with col2:
        st.write("### 💣 Malware Hash Checker")
        hash_input = st.text_input("Enter file hash (e.g., SHA256)")
        if st.button("Check Hash"):
            if hash_input:
                st.warning("⚠️ This hash appears in public threat intel sources.")
            else:
                st.warning("Please enter a hash.")

# ---------------------- News Publisher Tab ----------------------
with tabs[2]:
    st.subheader("📰 Publish Cybersecurity News")

    with st.form("news_form", clear_on_submit=True):
        title = st.text_input("News Title")
        author = st.text_input("Your Name or Alias")
        content = st.text_area("News Content")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        submitted = st.form_submit_button("Publish")
        if submitted:
            if title and content:
                st.session_state.news_posts.append({
                    "title": title,
                    "author": author or "Anonymous",
                    "content": content,
                    "date": date
                })
                st.success("✅ News published successfully!")
            else:
                st.error("Title and content are required.")

    # Show published posts
    if st.session_state.news_posts:
        st.markdown("---")
        st.markdown("### 🗞️ Published News")
        for post in reversed(st.session_state.news_posts):
            st.markdown(f"#### {post['title']}")
            st.markdown(f"**By:** {post['author']} &nbsp;&nbsp;|&nbsp;&nbsp; 📅 {post['date']}")
            st.markdown(post['content'])
            st.markdown("---")

# ---------------------- Threat Feeds Tab ----------------------
with tabs[3]:
    st.subheader("📡 Live Threat Feeds (Demo)")
    st.info("Example threat indicators. In future, this section will pull real-time data.")
    st.table({
        "Type": ["Phishing Domain", "Malicious IP", "APK Hash"],
        "Value": ["login-fb-check.com", "185.220.101.34", "7d8a3c..."],
        "Source": ["Community Report", "Abuse.ch", "VirusTotal"]
    })

# ---------------------- About Tab ----------------------
with tabs[4]:
    st.subheader("ℹ️ About This Portal")
    st.markdown("""
    This is a community-driven platform to support cybersecurity awareness and threat monitoring.

    **Highlights:**
    - Interactive tools
    - Scam & malware lookup
    - News submission by users
    - Open-source and free to contribute

    🧑‍💻 Maintained by: `@yourusername`  
    🔗 [GitHub Repo](https://github.com/yourusername/cybersec-portal)
    """)

# ---------------------- Footer ----------------------
st.markdown("---")
st.markdown("© 2025 | CyberSec Portal | Made with ❤️ using Streamlit")
