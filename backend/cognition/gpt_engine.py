import openai, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_message(profile_summary, goal):
    prompt = f"""
    Profile: {profile_summary}
    Goal: {goal}

    Generate a professional, personalized connection message (under 300 characters).
    """
    res = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message['content'].strip()
