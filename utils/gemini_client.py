# utils/gemini_client.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(prompt: str):
    try:
        # ✅ Use the correct model name from your list
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Test
if __name__ == "__main__":
    print("🤖 Asking Gemini...")
    result = ask_gemini("Summarize this log: Error at line 76. Socket closed unexpectedly.")
    print("✅ Gemini Response:", result)
