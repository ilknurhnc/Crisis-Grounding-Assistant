from app.services.profile_service import load_profile
from app.services.llm import generate_llm_grounding_response


def generate_grounding_response(message: str) -> str:
    profile = load_profile()

    try:
        return generate_llm_grounding_response(message, profile)

    except Exception:
        safe_phrases = profile.get("safe_phrases", [])
        helpful_activities = profile.get("helpful_activities", [])
        calming_colors = profile.get("calming_colors", [])

        selected_phrase = safe_phrases[0] if safe_phrases else "This feeling is temporary."
        selected_activity = helpful_activities[0] if helpful_activities else "take one slow breath"
        selected_color = calming_colors[0] if calming_colors else "a soft calming color"

        return (
            f"{selected_phrase} "
            f"Try to focus on {selected_color} around you, or imagine it gently surrounding you. "
            f"For the next minute, try this: {selected_activity}."
        )