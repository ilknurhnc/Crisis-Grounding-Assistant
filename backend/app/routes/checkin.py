from fastapi import APIRouter

from app.schemas import CheckInRequest, CheckInResponse
from app.services.grounding_service import generate_grounding_response


router = APIRouter(prefix="/checkin", tags=["check-in"])


@router.post("/", response_model=CheckInResponse)
def create_checkin(request: CheckInRequest):
    support_message = generate_grounding_response(request.message)

    return CheckInResponse(
        input_message=request.message,
        support_message=support_message
    )