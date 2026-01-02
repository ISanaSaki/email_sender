from fastapi import FastAPI
from app.api.routes import router as email_router

from app.db.session import engine
from app.db.base import Base
from app.db import models

app = FastAPI(title="Fake Email Sender")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(email_router)

@app.get("/")
def health_check():
    return {"status": "ok"}