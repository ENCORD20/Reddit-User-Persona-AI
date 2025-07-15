from utils import extract_username
from reddit_scraper import get_user_content
from persona_builder import build_persona_with_gemini
import os

def main():
    url = input("Enter Reddit profile URL: ")
    username = extract_username(url)
    if not username:
        print("❌ Invalid Reddit profile URL.")
        return

    print(f"🔍 Scraping posts/comments for user: {username}...")
    posts, comments = get_user_content(username)

    if not posts and not comments:
        print("⚠️ No data found for this user.")
        return

    print("🧠 Generating persona using google gemini...")
    persona, citations = build_persona_with_gemini(posts, comments)

    os.makedirs("output", exist_ok=True)
    output_file = f"output/{username}_persona.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"🧠 USER PERSONA: {username}\n\n")
        for p in persona:
            f.write(p + "\n\n")
        for c in citations:
            f.write(c + "\n")

    print(f"✅ Persona saved to: {output_file}")

if __name__ == "__main__":
    main()
