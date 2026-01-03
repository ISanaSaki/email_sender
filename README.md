# 📧 Email Sender (Fake)

A mini backend project for simulating email sending using async processing, rate limiting, and a task queue.

## 🚀 Description

This project provides a simple API endpoint to submit email sending requests.  
Requests are rate-limited, stored in PostgreSQL, and processed asynchronously using Celery and Redis.

> ⚠️ Email sending is fake and implemented only for learning purposes.

---

## 📌 API Endpoint

### POST /send-email

#### Request Body
```json
{
  "email": "user@example.com",
  "message": "Hello from FastAPI"
}