import os
from dotenv import load_dotenv
from openai import OpenAI

from app.prompts.grounding_prompt import SYSTEM_PROMPT


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_llm_grounding_response(message: str, profile: dict) -> str:
    user_prompt = f"""
User check-in:
{message}

User support profile:
Calming colors: {profile.get("calming_colors", [])}
Safe phrases: {profile.get("safe_phrases", [])}
Helpful activities: {profile.get("helpful_activities", [])}
Triggers: {profile.get("triggers", [])}

Generate a short personalized grounding response.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5,
        max_tokens=220
    )

    return response.choices[0].message.content