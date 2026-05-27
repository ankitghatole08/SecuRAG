import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


# ---------------------------------------------------
# CHECK OLLAMA STATUS
# ---------------------------------------------------
def check_ollama_status():

    print("🔍 Checking Ollama status...")

    try:
        response = requests.get(
            "http://127.0.0.1:11434/api/tags",
            timeout=5
        )

        print("✅ Ollama server detected")

        return response.status_code == 200

    except Exception as e:

        print("❌ Ollama not running")
        print(str(e))

        return False


# ---------------------------------------------------
# GENERATE AI SECURITY SUMMARY
# ---------------------------------------------------
def generate_ai_risk_summary(app, level, score):

    print("🔥 AI FUNCTION STARTED")

    # ---------------- ULTRA SHORT PROMPT ----------------
    prompt = f"""
App: {app.app_name}

Risk: {level}
Score: {score}

Internet: {app.internet_exposed}
Data: {app.data_classification}
Auth: {app.authentication_type}
Encryption: {app.encryption_enabled}

Give 1 short security warning and 1 short fix.
Max 20 words.
"""

    print("📨 Sending prompt to Ollama...")

    try:

        response = requests.post(
            OLLAMA_URL,
            json={

                # CHANGE THIS TO tinyllama
                "model": "tinyllama",

                "prompt": prompt,

                "stream": False,

                # FAST RESPONSE
                "temperature": 0.2,

                # VERY SHORT OUTPUT
                "num_predict": 30
            },

            # LONGER TIMEOUT
            timeout=300
        )

        print("📥 Response received from Ollama")

        data = response.json()

        ai_text = data.get("response", "").strip()

        print("🤖 AI OUTPUT:")
        print(ai_text)

        if ai_text == "":
            return "⚠ AI returned empty response"

        return ai_text

    except Exception as e:

        print("❌ AI GENERATION FAILED")
        print(str(e))

        return f"⚠ AI ERROR: {str(e)}"