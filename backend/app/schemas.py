from pydantic import BaseModel, Field


class CheckInRequest(BaseModel):
    message: str = Field(..., min_length=3)


class CheckInResponse(BaseModel):
    input_message: str
    support_message: str