from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.email import EmailCreate
from app.db.models import EmailRequest
from app.api.deps import get_db, rate_limit
from app.tasks.email import send_email_task

router = APIRouter()


@router.post("/send-email")
def send_email(
    data: EmailCreate,
    db: Session = Depends(get_db),
    _: None = Depends(rate_limit)
):
    email_request = EmailRequest(
        email=data.email,
        message=data.message,
        status="pending"
    )

    db.add(email_request)
    db.commit()
    db.refresh(email_request)

    send_email_task.delay(email_request.id)

    return {
        "message": "Email queued",
        "id": email_request.id,
        "status": email_request.status
    }