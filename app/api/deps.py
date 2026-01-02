from app.db.session import SessionLocal
from fastapi import Request, HTTPException
from app.core.redis import redis_client

RATE_LIMIT = 3
WINDOW_SECONDS = 60

def rate_limit(request: Request):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    current = redis_client.get(key)

    if current is None:
        redis_client.set(key, 1, ex=WINDOW_SECONDS)
        return

    if int(current) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many requests, try again later"
        )

    redis_client.incr(key)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()