from fastapi import APIRouter

from app.schemas import CheckInRequest, CheckInResponse


router = APIRouter(prefix="/checkin", tags=["check-in"])


@router.post("/", response_model=CheckInResponse)
def create_checkin(request: CheckInRequest):
    return CheckInResponse(
        input_message=request.message,
        support_message="I hear you. Take one slow breath and focus on one thing you can see right now."
    )