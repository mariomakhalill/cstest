import streamlit as st
import hashlib
import base64
import re
from datetime import datetime

# ---------------------- Page Config ----------------------
st.set_page_config(
    page_title="Cyber Tools Lab",
    layout="wide",
    page_icon="🛠️",
    initial_sidebar_state="expanded"
)

# ---------------------- Style ----------------------
st.markdown("""
    <style>
        .main { background-color: #0f1117; color: white; }
        h1, h2, h3, h4 { color: #61dafb; }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Tabs ----------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔢 Base64 Encode/Decode",
    "🔐 Hash Generator",
    "💣 XOR Encrypt/Decrypt",
    "🔍 Extractor",
    "📅 Epoch Converter"
])

# ---------------------- Base64 Encode/Decode ----------------------
with tab1:
    st.header("🔢 Base64 Encoder / Decoder")
    b64_mode = st.radio("Select Mode", ["Encode", "Decode"])
    b64_input = st.text_area("Enter Text")

    if st.button("Run Base64"):
        try:
            if b64_mode == "Encode":
                encoded = base64.b64encode(b64_input.encode()).decode()
                st.code(encoded)
            else:
                decoded = base64.b64decode(b64_input).decode()
                st.code(decoded)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# ---------------------- Hash Generator ----------------------
with tab2:
    st.header("🔐 Hash Generator (MD5, SHA1, SHA256)")
    text_to_hash = st.text_input("Enter text to hash")

    if st.button("Generate Hashes"):
        st.code(f"MD5    : {hashlib.md5(text_to_hash.encode()).hexdigest()}")
        st.code(f"SHA1   : {hashlib.sha1(text_to_hash.encode()).hexdigest()}")
        st.code(f"SHA256 : {hashlib.sha256(text_to_hash.encode()).hexdigest()}")

# ---------------------- XOR Encrypt/Decrypt ----------------------
with tab3:
    st.header("💣 XOR Encrypt / Decrypt")
    xor_text = st.text_area("Input text")
    xor_key = st.text_input("Key (1 character or more)")

    def xor_encrypt(text, key):
        return ''.join([chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text)])

    if st.button("Run XOR"):
        try:
            result = xor_encrypt(xor_text, xor_key)
            st.text("Result (may contain special chars):")
            st.code(result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# ---------------------- Extractor ----------------------
with tab4:
    st.header("🔍 Extract Emails, IPs, URLs")
    raw_input = st.text_area("Paste raw log or text")

    if st.button("Extract Now"):
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", raw_input)
        ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", raw_input)
        urls = re.findall(r"https?://[^\s]+", raw_input)

        st.write("📧 Emails:")
        st.code('\n'.join(emails) if emails else "None found")

        st.write("🌐 IPs:")
        st.code('\n'.join(ips) if ips else "None found")

        st.write("🔗 URLs:")
        st.code('\n'.join(urls) if urls else "None found")

# ---------------------- Epoch Converter ----------------------
with tab5:
    st.header("📅 Epoch Timestamp Converter")
    epoch_input = st.text_input("Enter UNIX timestamp (e.g., 1714788352)")

    if st.button("Convert Timestamp"):
        try:
            dt = datetime.fromtimestamp(int(epoch_input))
            st.success(f"Human-readable: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
        except:
            st.error("Invalid timestamp.")

# ---------------------- Footer ----------------------
st.markdown("---")
st.markdown("© 2025 | Cyber Tools Lab | Inspired by CyberChef")
