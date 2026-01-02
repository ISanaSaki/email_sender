import time
from app.core.celery_app import celery_app

@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 3})
def send_fake_email(self, email: str, message: str):
    print(f"Sending email to {email}")
    time.sleep(5) 
    print(f"Email sent to {email}")
    return "sent"