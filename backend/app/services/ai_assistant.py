import importlib
import json
import os
from typing import Any

# ===============================
# CONFIGURE GEMINI API
# ===============================
genai: Any = importlib.import_module("google.generativeai")
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")

genai.configure(api_key=api_key)

# Use stable fast model
model = genai.GenerativeModel("gemini-3-flash")


# ===============================
# MAIN FUNCTION
# ===============================
def ask_ai(question, wifi_data):
    wifi_data_text = wifi_data
    if not isinstance(wifi_data_text, str):
        wifi_data_text = json.dumps(wifi_data_text, indent=2, ensure_ascii=False)

    prompt = f"""
You are a professional WiFi network assistant.

Analyze this WiFi data:
{wifi_data_text}

Give:
1. Is it good for meetings?
2. Best time to use
3. Any issues

Keep answer short and in bullet points.

User Question: {question}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"