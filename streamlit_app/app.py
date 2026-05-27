import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="SecuRAG Dashboard",
    layout="wide"
)

st.title("🔐 SecuRAG Security Governance Dashboard")

st.markdown("AI-Powered Application Security Risk Assessment Platform")

st.divider()

# ---------------------------------------------------
# SIDEBAR STATUS
# ---------------------------------------------------
st.sidebar.title("🖥 System Status")

# Backend Status
try:
    backend = requests.get(f"{API_URL}/", timeout=3)

    if backend.status_code == 200:
        st.sidebar.success("✅ Backend Running")
    else:
        st.sidebar.error("❌ Backend Error")

except:
    st.sidebar.error("❌ Backend Offline")


# AI Status
try:
    ai = requests.get(
        "http://127.0.0.1:11434/api/tags",
        timeout=3
    )

    if ai.status_code == 200:
        st.sidebar.success("🤖 Ollama Running")
    else:
        st.sidebar.error("❌ Ollama Error")

except:
    st.sidebar.error("❌ Ollama Offline")


st.sidebar.divider()

st.sidebar.info(
    """
SecuRAG Features:

• AI Risk Analysis  
• Security Governance  
• Risk Scoring  
• AI Recommendations  
• Application Tracking  
"""
)

# ---------------------------------------------------
# APPLICATION FORM
# ---------------------------------------------------
st.header("📥 Add New Application")

with st.form("app_form"):

    col1, col2 = st.columns(2)

    with col1:
        app_name = st.text_input("Application Name")
        owner = st.text_input("Application Owner")
        cloud_provider = st.text_input("Cloud Provider")

    with col2:
        data_classification = st.selectbox(
            "Data Classification",
            ["public", "internal", "sensitive"]
        )

        internet_exposed = st.selectbox(
            "Internet Exposed",
            ["yes", "no"]
        )

        authentication_type = st.selectbox(
            "Authentication",
            ["password_only", "mfa"]
        )

        encryption_enabled = st.selectbox(
            "Encryption Enabled",
            ["yes", "no"]
        )

    submit = st.form_submit_button("🚀 Run AI Risk Assessment")


# ---------------------------------------------------
# FORM SUBMISSION
# ---------------------------------------------------
if submit:

    payload = {
        "app_name": app_name,
        "owner": owner,
        "cloud_provider": cloud_provider,
        "data_classification": data_classification,
        "internet_exposed": internet_exposed,
        "authentication_type": authentication_type,
        "encryption_enabled": encryption_enabled
    }

    # ---------------- LIVE STATUS ----------------
    status_box = st.empty()

    try:

        status_box.info("📡 Step 1/4 → Sending application data to backend...")
        time.sleep(1)

        status_box.info("🔍 Step 2/4 → Running security risk engine...")
        time.sleep(1)

        status_box.info("🤖 Step 3/4 → Generating AI security insights...")
        
        # ACTUAL API CALL
        res = requests.post(
            f"{API_URL}/applications/",
            json=payload,
            timeout=300
        )

        status_box.info("📊 Step 4/4 → Preparing dashboard results...")
        time.sleep(1)

        if res.status_code == 200:

            data = res.json()

            # SAVE ONLY LATEST RESULT
            st.session_state["latest_app"] = data

            status_box.success("✅ AI Risk Assessment Completed")

        else:
            status_box.error("❌ Backend Error")
            st.write(res.text)

    except Exception as e:

        status_box.error("❌ Request Failed")

        st.error(str(e))


# ---------------------------------------------------
# SHOW ONLY LATEST APPLICATION
# ---------------------------------------------------
if "latest_app" in st.session_state:

    data = st.session_state["latest_app"]

    st.divider()

    st.header("📊 Security Assessment Result")

    col1, col2, col3 = st.columns(3)

    # ---------------- COLUMN 1 ----------------
    with col1:

        st.metric(
            label="Risk Score",
            value=data.get("risk_score")
        )

        st.write("### 📌 Application Info")

        st.write("**Application:**", data.get("app_name"))
        st.write("**Owner:**", data.get("owner"))
        st.write("**Cloud:**", data.get("cloud_provider"))

    # ---------------- COLUMN 2 ----------------
    with col2:

        st.metric(
            label="Risk Level",
            value=data.get("risk_level")
        )

        st.write("### 🔐 Security Details")

        st.write(
            "**Data Classification:**",
            data.get("data_classification")
        )

        st.write(
            "**Internet Exposed:**",
            data.get("internet_exposed")
        )

        st.write(
            "**Authentication:**",
            data.get("authentication_type")
        )

    # ---------------- COLUMN 3 ----------------
    with col3:

        st.write("### 🤖 AI Security Analysis")

        st.info(
            data.get(
                "ai_summary",
                "No AI response"
            )
        )

    st.divider()

    # ---------------- RISK COLOR ----------------
    risk_level = data.get("risk_level")

    if risk_level == "Critical":
        st.error("🚨 Critical Risk Detected")

    elif risk_level == "High":
        st.warning("⚠ High Risk Application")

    elif risk_level == "Medium":
        st.info("🔍 Medium Risk Application")

    else:
        st.success("✅ Low Risk Application")