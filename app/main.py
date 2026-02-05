from fastapi import FastAPI
from app.api.routes import router as email_router

from app.db.session import engine
from app.db.base import Base
from app.db import models

app = FastAPI(title="Email Sender")
app.include_router(
    email_router,
    prefix="/api",
    tags=["Email"]
)
@app.get("/")
def health_check():
    return {"status": "ok"}