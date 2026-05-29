from typing import List
from pydantic import BaseModel, Field


class CheckInRequest(BaseModel):
    message: str = Field(..., min_length=3)


class CheckInResponse(BaseModel):
    input_message: str
    support_message: str


class ProfileRequest(BaseModel):
    calming_colors: List[str] = []
    safe_phrases: List[str] = []
    helpful_activities: List[str] = []
    triggers: List[str] = []


class ProfileResponse(BaseModel):
    message: str
    profile: ProfileRequest