import json
from pathlib import Path

from app.schemas import ProfileRequest


PROFILE_PATH = Path("../data/sample_profile.json")


def save_profile(profile: ProfileRequest) -> ProfileRequest:
    PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(PROFILE_PATH, "w", encoding="utf-8") as file:
        json.dump(profile.model_dump(), file, ensure_ascii=False, indent=4)

    return profile


def load_profile() -> dict:
    if not PROFILE_PATH.exists():
        return {
            "calming_colors": [],
            "safe_phrases": [],
            "helpful_activities": [],
            "triggers": []
        }

    with open(PROFILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)