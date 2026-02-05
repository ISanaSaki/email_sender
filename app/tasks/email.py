import time
from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.db.models import EmailRequest

@celery_app.task
def send_email_task(email_request_id: int):
    db = SessionLocal()

    try:
        email_request = db.query(EmailRequest).get(email_request_id)
        if not email_request:
            return "Email request not found"

        time.sleep(3)

        email_request.status = "sent"
        db.commit()

        return "Email sent"

    finally:
        db.close()