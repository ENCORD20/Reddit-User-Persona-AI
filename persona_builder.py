import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyBe5wcgBlAPickG3GqbgCKCR_qbIcDMRH8"))

GENERATION_MODEL = "gemini-2.5-flash"

def build_persona_with_gemini(posts, comments):
    all_text = "\n\n".join(
        [f"Post: {p['title']}\n{p['body']}" for p in posts] +
        [f"Comment: {c['body']}" for c in comments]
    )

    context = all_text[:16000]

    prompt = (
        "You are a social media analyst. Based on the following Reddit activity, "
        "generate a structured user persona with:\n"
        "- Interests\n- Communication style\n- Beliefs or values\n- Location (if mentioned)\n"
        "Include 1–2 quotes or post/comment links that support each trait.\n\n"
        f"{context}"
    )

    try:
        model = genai.GenerativeModel(GENERATION_MODEL)
        response = model.generate_content(prompt)
        output = response.text.strip()

        return output.split("\n\n"), ["Exit."]

    except Exception as e:
        print("❌ Gemini API Error:", e)
        return ["⚠️ Error calling Gemini API"], []
