from fastapi import APIRouter

from app.schemas import ProfileRequest, ProfileResponse
from app.services.profile_service import save_profile, load_profile


router = APIRouter(prefix="/profile", tags=["profile"])


@router.post("/", response_model=ProfileResponse)
def create_profile(profile: ProfileRequest):
    saved_profile = save_profile(profile)

    return ProfileResponse(
        message="Profile saved successfully.",
        profile=saved_profile
    )


@router.get("/")
def get_profile():
    return load_profile()