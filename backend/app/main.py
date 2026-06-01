from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import checkin, profile


app = FastAPI(
    title="InnerAnchor API",
    description="Context-aware grounding assistant backend.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(checkin.router)
app.include_router(profile.router)


@app.get("/")
def root():
    return {"message": "InnerAnchor API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}